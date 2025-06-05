from exceptions import TaskNotSupported

class HealthcareModule:
    def __init__(self):
        # Initialize healthcare-specific resources here
        pass

    def predict_disease(self, data):
        return "Disease prediction result"

    def herbal_treatment(self, data):
        return "Herbal treatment recommendation"

    def run_task(self, task, data):
        method = getattr(self, task, None)
        if method:
            return method(data)
        else:
            raise TaskNotSupported(f"Task '{task}' not supported in HealthcareModule.")
