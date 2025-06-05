from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict

# Import your AI core and exceptions
from agbako_ai import AgbakoAI, IndustryNotSupported, TaskNotSupported

app = FastAPI(
    title="AgbakoAI Modular API",
    description="AI API adaptable across industries, modular & scalable",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production, no wildcards for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI core once on startup
agbako_ai = AgbakoAI()

class TaskRequest(BaseModel):
    industry: str
    task: str
    data: Dict[str, Any]  # Arbitrary data input for flexibility

@app.get("/")
async def root():
    return {"message": "Welcome to AgbakoAI 🌍"}

@app.post("/ai/run-task")
async def run_task(request: TaskRequest):
    try:
        result = agbako_ai.run_task(request.industry, request.task, request.data)
        return {"industry": request.industry, "task": request.task, "result": result}
    except IndustryNotSupported as e:
        raise HTTPException(status_code=404, detail=str(e))
    except TaskNotSupported as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Catch-all for unexpected errors
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
