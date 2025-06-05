# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agbakoAI import AgbakoAI
import pandas as pd
import logging
from agbakoAI import AgbakoAI

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded from {file_path}.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        return None

def main():
    agbako_ai = AgbakoAI()
    data = load_data("your_dataset.csv")
    if data is None:
        return

    for task in ["train_model", "cross_validate", "hyperparameter_tuning"]:
        result = agbako_ai.run_task(task, "machine_learning", data)
        print(f"🔧 {task}: {result}")
app = FastAPI(
    title="AgbakoAI",
    description="Modular AI API adaptable across industries",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to AgbakoAI 🌍"}

@app.get("/ai/analyze")
async def analyze(text: str):
    ai = AgbakoAI()
    result = ai.run_task("analyze", "machine_learning", text)
    return {"input": text, "analysis": result}

if __name__ == "__main__":
    main()
