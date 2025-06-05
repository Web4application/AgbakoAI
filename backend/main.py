from fastapi import FastAPI, Depends, Request, WebSocket, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.auth import authenticate_user, create_access_token, get_current_user
from app.schemas import SymptomRequest
from app.database import SessionLocal, engine, Base
from app.models import AIRequestLog
from app.redis_cache import get_cached_treatment, set_cached_treatment
from app.ai_tasks import healthcare_predict_treatment
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user['username']}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict_treatment")
async def predict_treatment(data: SymptomRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cached = await get_cached_treatment(data.symptom)
    if cached:
        return cached
    treatment = await healthcare_predict_treatment(data.symptom)
    await set_cached_treatment(data.symptom, treatment)

    log = AIRequestLog(symptom=data.symptom, treatment=treatment["treatment"])
    db.add(log)
    db.commit()

    return treatment

@app.websocket("/ws/progress")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    for i in range(101):
        await websocket.send_text(f"Progress: {i}%")
        await asyncio.sleep(0.05)
    await websocket.close()
