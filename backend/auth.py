from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import importlib

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_verify_token(token: str):
    # Replace with real token validation logic
    if token != "supersecrettoken":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    fake_verify_token(token)
    return {"username": "authorized_user"}

class TaskRequest(BaseModel):
    data: dict

@app.post("/ai/run-task")
async def run_task(
    industry: str,
    task: str,
    task_request: TaskRequest,
    user=Depends(get_current_user)
):
    try:
        module_name, class_name = {
            'healthcare': ('modules.healthcare', 'HealthcareModule'),
            'finance': ('modules.finance', 'FinanceModule'),
            'education': ('modules.education', 'EducationModule'),
            'marketing': ('modules.marketing', 'MarketingModule'),
        }[industry]
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid industry")

    module = importlib.import_module(module_name)
    module_class = getattr(module, class_name)
    ai_module = module_class()

    if not hasattr(ai_module, task):
        raise HTTPException(status_code=400, detail=f"Task {task} not supported")

    func = getattr(ai_module, task)
    result = func(task_request.data)

    return {"result": result}
