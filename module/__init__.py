import importlib
from exceptions import IndustryNotSupported, TaskNotSupported

class AgbakoAI:
    def __init__(self):
        # Tuple format: ('module.path', 'ClassName')
        self.module_info = {
            'healthcare': ('modules.healthcare', 'HealthcareModule'),
            'finance': ('modules.finance', 'FinanceModule'),
            'education': ('modules.education', 'EducationModule'),
            'marketing': ('modules.marketing', 'MarketingModule'),
            'agriculture':('moddules.agriculture', 'crop_predictionModule'),
            'science':('modules.science', 'disease_predictionMidule'),
        }
        self.modules = {}

    def get_module(self, industry):
        if industry not in self.modules:
            if industry not in self.module_info:
                raise IndustryNotSupported(f"Industry '{industry}' not supported yet.")
            
            module_path, class_name = self.module_info[industry]
            module = importlib.import_module(module_path)
            klass = getattr(module, class_name)
            self.modules[industry] = klass()
        return self.modules[industry]

    def run_task(self, industry, task, data):
        module = self.get_module(industry)
        method = getattr(module, task, None)
        if not method:
            raise TaskNotSupported(f"Task '{task}' not supported in {industry} module.")
        return method(data)
