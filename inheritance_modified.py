class BasePlugin:
    def __init__(self, name: str, developer: str):
        self.name = name
        self.developer = developer
        print(f"[{self.name}] Initialized by parent class.")

class ImagePlugin(BasePlugin):
    def __init__(self, name: str, developer: str, supported_format: str):
        # super() invokes the __init__ of BasePlugin to set name and developer
        super().__init__(name, developer) 
        
        # New, specific attribute belonging only to the child class
        self.supported_format = supported_format
        print(f"[{self.name}] Specific format set to: {self.supported_format}")

# Execution
img_tool = ImagePlugin(name="PNG Optimizer", developer="DevCorp", supported_format="PNG")
