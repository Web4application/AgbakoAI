import asyncio
import importlib
import pkgutil
import logging
from exceptions import IndustryNotSupported, TaskNotSupported

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgbakoAI")

# Decorator for task registration
def ai_task(func):
    func.is_ai_task = True
    return func

class BaseModule:
    def __init__(self):
        self._tasks = {
            name: method for name, method in vars(self.__class__).items()
            if callable(method) and getattr(method, 'is_ai_task', False)
        }

    def get_tasks(self):
        return list(self._tasks.keys())

    async def run_task(self, task, data):
        method = self._tasks.get(task)
        if method is None:
            raise TaskNotSupported(f"Task '{task}' not supported in {self.__class__.__name__}")
        if asyncio.iscoroutinefunction(method):
            return await method(self, data)
        else:
            # Support sync methods as well
            return method(self, data)


# Example industry modules inside a `modules` package/folder

class HealthcareModule(BaseModule):
    def __init__(self):
        super().__init__()
        # Initialize healthcare-specific resources here

    @ai_task
    async def predict_disease(self, data):
        await asyncio.sleep(0.1)  # simulate async call to AI model
        return "Disease prediction result"

    @ai_task
    def herbal_treatment(self, data):
        return "Herbal treatment recommendation"


class FinanceModule(BaseModule):
    def __init__(self):
        super().__init__()
        # Initialize finance-related resources here

    @ai_task
    async def predict_stock(self, data):
        await asyncio.sleep(0.1)  # simulate async call
        return "Stock prediction result"

    @ai_task
    def detect_fraud(self, data):
        return "Fraud detection result"


# Add other industry modules here...

class AgbakoAI:
    def __init__(self):
        self.modules = {}
        self.module_classes = self.discover_modules()
        logger.info(f"Discovered modules: {list(self.module_classes.keys())}")

    def discover_modules(self):
        modules = {}
        for finder, name, ispkg in pkgutil.iter_modules(['modules']):
            try:
                mod = importlib.import_module(f"modules.{name}")
                cls_name = f"{name.capitalize()}Module"
                cls = getattr(mod, cls_name, None)
                if cls:
                    modules[name] = cls
            except Exception as e:
                logger.error(f"Error importing module '{name}': {e}")
        return modules

    def get_module(self, industry):
        if industry not in self.modules:
            if industry not in self.module_classes:
                raise IndustryNotSupported(f"Industry '{industry}' not supported yet.")
            self.modules[industry] = self.module_classes[industry]()
        return self.modules[industry]

    async def run_task(self, industry, task, data):
        try:
            module = self.get_module(industry)
            result = await module.run_task(task, data)
            self.log_usage(industry, task, success=True)
            return result
        except (IndustryNotSupported, TaskNotSupported) as e:
            self.log_usage(industry, task, success=False, error=str(e))
            raise
        except Exception as e:
            self.log_usage(industry, task, success=False, error=f"Unexpected: {e}")
            logger.error(f"Unexpected error: {e}")
            raise

    def log_usage(self, industry, task, success, error=None):
        # TODO: Hook this to analytics service or DB
        status = "SUCCESS" if success else "FAIL"
        logger.info(f"[{status}] Industry: {industry}, Task: {task}, Error: {error}")

    # Example of an API key check (mock)
    def check_access(self, api_key, industry, task):
        # TODO: Implement real API key auth and RBAC here
        allowed = True  # Replace with actual logic
        if not allowed:
            raise PermissionError("Access denied.")

# Example driver code with async main

async def main():
    agbako_ai = AgbakoAI()

    try:
        res = await agbako_ai.run_task('healthcare', 'predict_disease', {"patient_info": "data"})
        print(res)

        res2 = await agbako_ai.run_task('finance', 'detect_fraud', {"transaction": "data"})
        print(res2)

        # Try unsupported industry
        await agbako_ai.run_task('tech', 'predict_trends', {"data": "data"})

    except IndustryNotSupported as e:
        print(f"Error: {e}")

    try:
        # Try unsupported task
        await agbako_ai.run_task('finance', 'predict_trends', {"stock_data": "data"})
    except TaskNotSupported as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
