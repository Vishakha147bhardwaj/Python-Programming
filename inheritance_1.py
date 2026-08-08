# The Parent Class (General Blueprint)
class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.status = "Idle"

    def report_status(self):
        print(f"Agent {self.name} is currently {self.status}.")

# The Child Class (Specialized Blueprint inheriting from BaseAgent)
class SupportAgent(BaseAgent):
    def __init__(self, name, language):
        # Call the parent's __init__ to set up the name and status
        super().__init__(name) 
        # Add a new attribute unique ONLY to Support Agents
        self.language = language 

    # A brand new method unique to Support Agents
    def resolve_ticket(self, ticket_id):
        self.status = "Working"
        print(f"[{self.name}] Resolving customer ticket #{ticket_id} in {self.language}.")
        self.status = "Idle"

# --- Deployment ---
generic_bot = BaseAgent("Bot-01")
chat_bot = SupportAgent("Helper-Bot", "Spanish")

generic_bot.report_status()
# chat_bot can use parent methods AND its own unique methods
chat_bot.report_status() 
chat_bot.resolve_ticket(404)
