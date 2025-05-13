import random

class TrialSimulator:
    def __init__(self):
        self.success_rate = 0.8  # Default success rate for new trials

    def simulate_trial(self, treatment):
        outcome = random.random()
        if outcome < self.success_rate:
            return f"Success: {treatment} is effective."
        else:
            return f"Failure: {treatment} is not effective."
