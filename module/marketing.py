from exceptions import TaskNotSupported

class MarketingModule:
    def __init__(self):
        # Initialize marketing-specific resources
        pass

    def campaign_optimization(self, data):
        return "Marketing campaign optimization result"

    def customer_segmentation(self, data):
        return "Customer segmentation result"

    def run_task(self, task, data):
        method = getattr(self, task, None)
        if method:
            return method(data)
        else:
            raise TaskNotSupported(f"Task '{task}' not supported in MarketingModule.")
