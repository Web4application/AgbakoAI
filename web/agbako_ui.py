from flask import Flask, render_template, request, jsonify
import requests

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import importlib

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_verify_token(token: str):
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

    try:
        module = importlib.import_module(module_name)
        module_class = getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        raise HTTPException(status_code=500, detail=f"Module load error: {str(e)}")

    ai_module = module_class()

    if not hasattr(ai_module, task):
        raise HTTPException(status_code=400, detail=f"Task '{task}' not supported in {industry}")

    func = getattr(ai_module, task)

    # Support async tasks too
    if callable(func):
        if callable(getattr(func, "__await__", None)):
            result = await func(task_request.data)
        else:
            result = func(task_request.data)
    else:
        raise HTTPException(status_code=400, detail=f"Task '{task}' is not callable")

    return {"result": result}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_treatment', methods=['POST'])
def get_treatment():
    symptom = request.form.get('symptom', '')
    try:
        response = requests.post(
            'http://localhost:5000/predict_treatment',
            json={"symptom": symptom},
            timeout=5
        )
        response.raise_for_status()
        prediction = response.json()
        return jsonify(prediction)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to get treatment prediction", "details": str(e)}), 500
