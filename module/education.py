from exceptions import TaskNotSupported

class EducationModule:
    def __init__(self):
        # Initialize education-specific resources
        pass

    def predict_student_performance(self, data):
        return "Student performance prediction result"

    def recommend_personalized_learning(self, data):
        return "Personalized learning recommendation"

    def run_task(self, task, data):
        method = getattr(self, task, None)
        if method:
            return method(data)
        else:
            raise TaskNotSupported(f"Task '{task}' not supported in EducationModule.")
