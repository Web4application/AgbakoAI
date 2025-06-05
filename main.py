from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_treatment", response_class=HTMLResponse)
async def get_treatment(request: Request, symptom: str = Form(...)):
    treatment = "Take ibuprofen and rest" if "fever" in symptom.lower() else "Consult a doctor"
    return templates.TemplateResponse("result.html", {"request": request, "treatment": treatment})
