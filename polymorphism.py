
class CalculatorTool:
    def activate(self, query):
        return f"Calculating math for: {query}"


class WebSearchTool:
    def activate(self, query):
        return f"Searching Google for live results on: {query}"

def run_agent_tool(tool_object, user_request):
  
    result = tool_object.activate(user_request)
    print(result)


math_tool = CalculatorTool()
search_tool = WebSearchTool()

run_agent_tool(math_tool, "55 * 430")      
run_agent_tool(search_tool, "AI News 2026") 


# # Tool 1: Calculator Plugin
# class CalculatorTool:
#     def activate(self, query):
#         # Specific behavior: Math
#         return f"[Calculator Result] Evaluated math expression: {query} = {eval(query)}"

# # Tool 2: Web Search Plugin
# class WebSearchTool:
#     def activate(self, query):
#         # Specific behavior: Searching internet
#         return f"[Search Result] Browsing the web for: '{query}'... Found 3 relevant articles."

# # Tool 3: Image Generator Plugin
# class ImageGenTool:
#     def activate(self, query):
#         # Specific behavior: Creating art
#         return f"[Image Result] Rendering high-quality graphic matching prompt: '{query}'."

# # --- The Core AI Agent Engine ---
# class CoreAIEngine:
#     def __init__(self):
#         self.toolkit = []

#     def load_tool(self, tool_object):
#         self.toolkit.append(tool_object)

#     def run_all_diagnostics(self, test_prompt):
#         print("--- Initiating Tool Toolkit Check ---")
#         # Polymorphism in action: Loop through different tools and run the SAME method name
#         for tool in self.toolkit:
#             result = tool.activate(test_prompt)
#             print(result)

# # --- Deployment ---
# # 1. Create the master engine
# ai_brain = CoreAIEngine()

# # 2. Instantiate different types of tools
# math_plugin = CalculatorTool()
# search_plugin = WebSearchTool()
# art_plugin = ImageGenTool()

# # 3. Plug them into the toolkit
# ai_brain.load_tool(math_plugin)
# ai_brain.load_tool(search_plugin)
# ai_brain.load_tool(art_plugin)

# # 4. Fire the single trigger command
# # Notice how one method call runs completely different logic for each tool!
# ai_brain.run_all_diagnostics("2 + 2")
