#!/bin/bash

set -e

echo "Creating project structure..."

mkdir -p agbakoai-backend/modules
cd agbakoai-backend

echo "Writing main.py..."

cat > main.py <<'EOF'
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import importlib

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fake user store - replace with DB or real user system
fake_users_db = {
    "admin": {"username": "admin", "password": "secret", "token": "supersecrettoken"}
}

def verify_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return user
    return None

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = None
    for u in fake_users_db.values():
        if u["token"] == token:
            user = u
            break
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    return user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user["token"], "token_type": "bearer"}

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

    if callable(func):
        if callable(getattr(func, "__await__", None)):
            result = await func(task_request.data)
        else:
            result = func(task_request.data)
    else:
        raise HTTPException(status_code=400, detail=f"Task '{task}' is not callable")

    return {"result": result}
EOF

echo "Writing sample industry modules..."

cat > modules/healthcare.py <<'EOF'
class HealthcareModule:
    def diagnosis(self, data):
        symptoms = data.get("symptoms", [])
        if "fever" in symptoms:
            return "Take ibuprofen and rest."
        return "Consult a healthcare professional."

    async def async_task_example(self, data):
        import asyncio
        await asyncio.sleep(1)
        return {"message": "Async task completed", "input": data}
EOF

cat > modules/finance.py <<'EOF'
class FinanceModule:
    def forecast(self, data):
        return {"forecast": "Market trends are bullish."}
EOF

cat > modules/education.py <<'EOF'
class EducationModule:
    def recommend_course(self, data):
        interests = data.get("interests", [])
        if "AI" in interests:
            return "Enroll in Advanced AI course."
        return "Explore general education programs."
EOF

cat > modules/marketing.py <<'EOF'
class MarketingModule:
    def campaign_strategy(self, data):
        target = data.get("target_audience", "general public")
        return f"Designing a campaign for {target}."
EOF

touch modules/__init__.py

echo "Setting up virtual environment and installing dependencies..."

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install fastapi uvicorn python-multipart

echo "Setup complete! To run your API server, do:"
echo "source venv/bin/activate"
echo "uvicorn main:app --reload"

cd ..
