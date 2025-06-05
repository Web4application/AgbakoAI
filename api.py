from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agbako_ai import AgbakoAI, IndustryNotSupported, TaskNotSupported

app = FastAPI()
agbako_ai = AgbakoAI()

class TaskRequest(BaseModel):
    industry: str
    task: str
    data: dict

@app.post("/run-task")
def run_task(request: TaskRequest):
    try:
        result = agbako_ai.run_task(request.industry, request.task, request.data)
        return {"result": result}
    except IndustryNotSupported as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TaskNotSupported as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Catch-all for unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
