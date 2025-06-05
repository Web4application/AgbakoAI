from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from agbakoAI import AgbakoAI, IndustryNotSupported, TaskNotSupported
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(
    title="AgbakoAI",
    description="Modular AI API adaptable across industries",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Make this more strict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai = AgbakoAI()  # Global instance for reuse

@app.get("/")
async def read_root():
    return {"message": "Welcome to AgbakoAI 🌍"}

@app.get("/ai/run-task/")
async def run_task(
    industry: str = Query(..., example="healthcare"),
    task: str = Query(..., example="predict_disease"),
    data: str = Query(..., example="{'patient_info': 'data'}")
):
    try:
        # You can later parse `data` into JSON if your modules require dicts
        result = ai.run_task(industry, task, {"input": data})
        return {"result": result}
    except (IndustryNotSupported, TaskNotSupported) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.exception("Unhandled error")
        raise HTTPException(status_code=500, detail="Internal server error")
