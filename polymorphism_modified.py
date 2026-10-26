class TextLowerTool:
    def execute(self, data: str) -> str:
        return data.lower()

class TextReverseTool:
    def execute(self, data: str) -> str:
        return data[::-1]

# Execution
# Both objects are entirely different classes, but have the same interface (.execute())
tools = [TextLowerTool(), TextReverseTool()]
sample_input = "Hello OOP World"

for tool in tools:
    # Polymorphism in action: The loop handles both objects identically
    result = tool.execute(sample_input)
    print(f"Processed Output: {result}")
