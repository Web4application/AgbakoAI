from exceptions import TaskNotSupported

class FinanceModule:
    def __init__(self):
        # Initialize finance-related resources here
        pass

    def predict_stock(self, data):
        return "Stock prediction result"

    def detect_fraud(self, data):
        return "Fraud detection result"

    def run_task(self, task, data):
        method = getattr(self, task, None)
        if method:
            return method(data)
        else:
            raise TaskNotSupported(f"Task '{task}' not supported in FinanceModule.")
