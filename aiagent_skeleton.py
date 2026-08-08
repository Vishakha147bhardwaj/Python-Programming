class AIAgent:
    # 1. Setup Wizard: Give the agent a identity and an empty brain (memory)
    def __init__(self, agent_name, specialized_skill):
        self.name = agent_name
        self.skill = specialized_skill
        self.memory_bank = [] # Starts empty

    # 2. Method (Action): Look at the world and remember things
    def read_environment(self, current_situation):
        print(f"[{self.name}] observing: {current_situation}")
        self.memory_bank.append(current_situation)

    # 3. Method (Action): Make a decision based on what it remembers
    def take_action(self):
        if "low battery" in self.memory_bank:
            return f"Action: [{self.name}] is moving to the charging station."
        else:
            return f"Action: [{self.name}] is continuing to perform: {self.skill}."

# --- LET'S BUILD THE AGENT IN REAL LIFE ---
vacuum_bot = AIAgent("Roomba-X", "Floor Cleaning")

# Agent reads the room
# vacuum_bot.read_environment("The living room rug is dirty")
vacuum_bot.read_environment("low battery")

# Agent makes a decision
next_move = vacuum_bot.take_action()
print(next_move) 
# Output: Action: [Roomba-X] is moving to the charging station.
