import pandas as pd
import logging
from agbakoAI import AgbakoAI  # Assuming agbakoAI.py is in the same directory
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="AgbakoAI",
    description="Modular AI API adaptable across industries",
    version="0.1.0",
)

# Configure CORS (modify as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific domains in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example root route
@app.get("/")
async def read_root():
    return {"message": "Welcome to AgbakoAI 🌍"}

# Placeholder route for an AI module
@app.get("/ai/analyze")
async def analyze(text: str):
    return {"input": text, "analysis": "🧠 This is a placeholder 
# Setup logging for better visibility
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """Load and preprocess data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded from {file_path}.")
        return data
    except Exception as e:
        logging.error(f"Error loading data from {file_path}: {str(e)}")
        return None

def main():
    """Main entry point for AgbakoAI system."""
    
    # Initialize the AgbakoAI system
    agbako_ai = AgbakoAI()
    
    # Example: Load data (adjust the file path as needed)
    data_file = 'your_dataset.csv'  # Replace with your dataset path
    data = load_data(data_file)
    
    if data is None:
        logging.error("Data could not be loaded, exiting the program.")
        return
    
    # Example: Run a machine learning task
    task = 'train_model'  # You can change this to 'evaluate_model', 'cross_validate', etc.
    industry = 'machine_learning'  # Can be 'machine_learning', 'finance', etc.
    
    # Run the task on the selected industry
    result = agbako_ai.run_task(task, industry, data)
    print(result)  # Output the result of the task
    
    # Example: Run a cross-validation task
    task = 'cross_validate'
    result = agbako_ai.run_task(task, industry, data)
    print(result)  # Output the cross-validation result

    # Example: Hyperparameter tuning task
    task = 'hyperparameter_tuning'
    result = agbako_ai.run_task(task, industry, data)
    print(result)  # Output the result of hyperparameter tuning

if __name__ == "__main__":
    main()
