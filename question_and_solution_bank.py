# 📐 Part 1: Functions & Scope
# Question 1 (Easy): Default Arguments & Type SafetyStatement:
#  Write a function generate_api_url(endpoint, base_url="https://example.com", 
# version="v1") that constructs a full URL string by joining the inputs in the format: {base_url}/{version}/{endpoint}. 
# If the endpoint starts with a forward slash /, strip it before joining to prevent double slashes.
def generate_api_url(endpoint: str, base_url: str = "https://example.com", version: str = "v1") -> str:
    if endpoint.startswith("/"):
        endpoint = endpoint[1:]
    return f"{base_url}/{version}/{endpoint}"

# Test
print(generate_api_url("/users")) 

# Question 2 (Easy): Lambda Functions for Data MappingStatement:
#  Given a list of product dictionaries containing keys "name" and "price", 
# write a single-line lambda function assigned to a variable named extract_prices 
# that extracts only the numeric prices from the list using Python's built-in map() function.
#  Convert the map object to a list before returning.
# Solution:
def generate_api_url(endpoint: str, base_url: str = "https://example.com", version: str = "v1") -> str:
    if endpoint.startswith("/"):
        endpoint = endpoint[1:]
    return f"{base_url}/{version}/{endpoint}"

# Test
print(generate_api_url("/users"))  

# Question 3 (Medium): Positional Argument Aggregation via *argsStatement:
#  Create a function calculate_shipping_weight(base_box_weight, *item_weights) 
# that adds up all positional item arguments passed after the base box weight parameter. 
# However, if any individual item weight parameter is less than 0.1 kg, skip adding it and print a warning message.

# Solution:
def calculate_shipping_weight(base_box_weight: float, *item_weights: float) -> float:
    total = base_box_weight
    for weight in item_weights:
        if weight < 0.1:
            print(f"Warning: Item weight {weight} too light, skipping.")
            continue
        total += weight
    return total

# Test
print(calculate_shipping_weight(0.5, 10.2, 0.05, 4.3))  # Expected: 15.0 

# Question 4 (Medium): Keyword Argument Configurations via **kwargsStatement:
#  Write a function build_html_tag(tag_name, content, **attributes) that constructs
#  a raw HTML element string. The function must unpack the variable keyword arguments 
# container to generate inline key-value attribute assignments within the opening tag.

# Solution:
def build_html_tag(tag_name: str, content: str, **attributes) -> str:
    attrs_str = ""
    for key, value in attributes.items():
        attrs_str += f' {key}="{value}"'
    return f"<{tag_name}{attrs_str}>{content}</{tag_name}>"

# Test
print(build_html_tag("a", "Click Here", href="https://google.com", target="_blank"))
# Expected: <a href="https://google.com" target="_blank">Click Here</a>

# Question 5 (Medium): Local vs Global Scope IsolationStatement:
#  Write a logging utility system that tracks an internal operational
#  state using a global counter sequence variable API_CALL_COUNT. 
# Implement a function increment_api_counter() that modifies this global 
# variable directly from within its local block scope execution layer without 
# creating a new local shadow pointer reference.

# Solution:
API_CALL_COUNT = 0

def increment_api_counter():
    global API_CALL_COUNT
    API_CALL_COUNT += 1

# Test
increment_api_counter()
increment_api_counter()
print(API_CALL_COUNT)  # Expected: 2

# 🌐 Part 2: Regular Expressions & Async Basics
# Question 6 (Easy): Text Subsystem Replacement via re.sub()Statement: 
# Web scrapers frequently grab strings cluttered with nested structural elements. 
# Write a python script using re.sub() that strips out all raw markdown-style hyperlinks 
# from a block of text, replacing them completely with the raw text sequence inside the square brackets.

# Solution:
import re
def strip_markdown_links(text: str) -> str:
    # Matches [Text](URL) and replaces it with group 1 (Text)
    pattern = r'\[([^\]]+)\]\([^)]+\)'
    return re.sub(pattern, r'\1', text)

# Test
sample = "Please read the [Terms of Service](https://example.com) and [Privacy Policy](https://example.com)."
print(strip_markdown_links(sample))
# Expected: "Please read the Terms of Service and Privacy Policy."

# Question 7 (Easy): Coordinate Extraction via re.findall()Statement:
#  Extract structured configuration coordinates from log files. 
# Write a function extract_coordinates(log_data) using re.findall() to
#  return a list of parsed integer coordinate pair tuples (X, Y) matching 
# the string footprint template format LOC[X,Y].

# Solution:
def extract_coordinates(log_data: str) -> list:
    pattern = r'LOC\[(\d+),(\d+)\]'
    matches = re.findall(pattern, log_data)
    # Convert string match outputs to numeric integer tuples
    return [(int(x), int(y)) for x, y in matches]

# Test
logs = "Error at LOC[10,25] followed by warning notice at LOC[400,90]."
print(extract_coordinates(logs))  # Expected: [(10, 25), (400, 90)]


# Question 8 (Medium): Pattern Extraction Checks via re.search()Statement:
#  Parse unstructured raw header logs to validate form structure input components.
#  Write a text pattern validation wrapper function validate_product_sku(sku_string) 
# that checks if a string strictly follows the format structure rule: Exactly 3 capital letters,
#  followed by a hyphen, followed by exactly 4 numeric integer characters (e.g., PRO-1024).

# Solution:
def validate_product_sku(sku_string: str) -> bool:
    # Use ^ and $ anchors to match the entire string length strictly
    pattern = r'^[A-Z]{3}-\d{4}$'
    if re.search(pattern, sku_string):
        return True
    return False

# Test
print(validate_product_sku("ABC-1234"))  # Expected: True
print(validate_product_sku("abC-1234"))  # Expected: False

# Question 9 (Medium): Basic Concurrent Timers via asyncioStatement: 
# Create an asynchronous script structure engine containing an async routine 
# named fetch_api_metadata(service_name, delay_seconds). The process should print a 
# starting notice statement, non-blockingly suspend its execution timeline for the 
# specified timeframe using asyncio.sleep(), and then print a completion string before 
# returning a mock status indicator payload dictionary.


# Solution:
import asyncio
async def fetch_api_metadata(service_name: str, delay_seconds: int) -> dict:
    print(f"[+] Launching network pipeline task stream for: {service_name}")
    await asyncio.sleep(delay_seconds)
    print(f"[✓] Metadata retrieval finished for: {service_name}")
    return {"service": service_name, "status": "200_OK"}

# Execution run inside VS Code main block loop:
# asyncio.run(fetch_api_metadata("AuthService", 2))

# Question 10 (Medium): Parallel Task Concurrency via asyncio.gather()Statement:
#  Build an async entrypoint script function run_parallel_scrapers() that launches 
# three separate instances of the fetch_api_metadata utility block from Question 9 
# concurrently. Execute them simultaneously with delay metrics of 3, 1, and 2 seconds,
#  collecting the final result payloads array into a combined output pool using asyncio.gather().


# Solution:
async def run_parallel_scrapers() -> list:
    task1 = fetch_api_metadata("Scraper_A", 3)
    task2 = fetch_api_metadata("Scraper_B", 1)
    task3 = fetch_api_metadata("Scraper_C", 2)
    
    # Run all three concurrently. Total runtime will equal the longest delay (3 seconds)
    combined_results = await asyncio.gather(task1, task2, task3)
    return combined_results

# Test execution runner context
# print(asyncio.run(run_parallel_scrapers()))


# 📥 OOP — Part 1: Core Components & Agent Skeletons(Classes, __init__, self, attributes, methods, and an Agent class skeleton)

# 1. The Setup: Creating the Basic Agent Skeleton 🟢 (Easy)
# Problem Statement:
# Create a foundational Agent class. 
# It should accept two arguments upon initialization: name (a string) and model (a string like "gpt-4").
#  Store these as instance variables. Add an instance method called introduce() that returns a string 
# formatted exactly like: "Hello, I am Agent [name] powered by [model]."

# Solution:
class Agent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    def introduce(self):
        return f"Hello, I am Agent {self.name} powered by {self.model}."

# Testing the implementation
my_agent = Agent(name="Nexus", model="Claude-3")
print(my_agent.introduce())
# Output: Hello, I am Agent Nexus powered by Claude-3.

# 2. Monitoring Costs: State Management with Attributes 🟡 (Medium)
# Problem Statement:
# AI agents accumulate runtime costs. Modify or write an Agent class that starts with an internal
#  counter tracking total API tokens processed (total_tokens). Initialize it to 0. Create a method
#  called process_request(tokens_used) that accepts an integer, adds it to the running total, and 
# returns the updated total_tokens.

# Solution:
class Agent:
    def __init__(self, name):
        self.name = name
        self.total_tokens = 0  # Initialized to zero automatically
        
    def process_request(self, tokens_used):
        self.total_tokens += tokens_used
        return self.total_tokens

# Testing the implementation
runner = Agent("TaskBot")
runner.process_request(150)
runner.process_request(250)
print(f"Tokens consumed: {runner.total_tokens}")
# Output: Tokens consumed: 400

# 3. Agent Personality: Dynamic Attributes via self 🟢 (Easy)
# Problem Statement:
# Create a PersonaAgent class. In its initialization, accept a parameter called temperature 
# (a float representing creativity). Write a method called set_creativity(new_temp) that allows 
# you to dynamically modify this property on the active instance using self.

# Solution:
class PersonaAgent:
    def __init__(self, temperature):
        self.temperature = temperature
        
    def set_creativity(self, new_temp):
        self.temperature = new_temp

# Testing the implementation
agent = PersonaAgent(0.2)
print(f"Original: {agent.temperature}") # Output: 0.2
agent.set_creativity(0.7)
print(f"Updated: {agent.temperature}")  # Output: 0.7


# 4. Memory Log: Appending to List Attributes 🟡 (Medium)
# Problem Statement:Agents need conversation history. Create an AgentWithMemory class.
#  Initialize a property called chat_history as an empty list inside __init__. Write a method 
# remember(role, message) that creates a dictionary keying those two strings (e.g., {"role": role, "message": message}) 
# and appends it to the memory history list.

# Solution:
class AgentWithMemory:
    def __init__(self):
        self.chat_history = [] # Dynamic collection tracking state
        
    def remember(self, role, message):
        turn = {"role": role, "message": message}
        self.chat_history.append(turn)

# Testing the implementation
brain = AgentWithMemory()
brain.remember("user", "What is 2+2?")
brain.remember("assistant", "It is 4.")
print(brain.chat_history)
# Output: [{'role': 'user', 'message': 'What is 2+2?'}, {'role': 'assistant', 'message': 'It is 4.'}]


# 5. Final Assembly: The Full AI Agent Action Loop 🟡 (Medium)
# Problem Statement:
# Build a cohesive ActionAgent that tracks context and performs operations.
#  The agent should contain an initialization parameter system_prompt. 
# Write a method called execute(user_input) that returns a formatted string simulating an 
# AI output combination: "System: [system_prompt] | User: [user_input] -> Executing response..."

# Solution:
class ActionAgent:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        
    def execute(self, user_input):
        return f"System: {self.system_prompt} | User: {user_input} -> Executing response..."

# Testing the implementation
coder_agent = ActionAgent("You are a senior python engineer.")
result = coder_agent.execute("Write a loop.")
print(result)
# Output: System: You are a senior python engineer. | User: Write a loop. -> Executing response...


# 🧬 OOP — Part 2: Advanced Mechanics & Extensibility(Inheritance, super(), encapsulation, dunder methods, and Polymorphism for plugins)
# 6. Specialization: Utilizing super() in Inheritance 🟢 (Easy)
# Problem Statement:
# You have a base class BaseAgent with an __init__ that takes a name.
#  Create a child class called VisionAgent that inherits from BaseAgent. 
# Use super().__init__(name) to properly initialize the base name attribute, but also accept and
#  assign a unique subclass attribute called camera_resolution (a string).

# Solution:
class BaseAgent:
    def __init__(self, name):
        self.name = name

class VisionAgent(BaseAgent):
    def __init__(self, name, camera_resolution):
        # Call the parent constructor to set up the inherited property
        super().__init__(name)
        self.camera_resolution = camera_resolution

# Testing the implementation
eye_bot = VisionAgent("Argus", "4K")
print(f"Agent {eye_bot.name} operates at resolution {eye_bot.camera_resolution}.")
# Output: Agent Argus operates at resolution 4K.


# 7. Protecting Secrets: Variable Encapsulation 🟡 (Medium)
# Problem Statement:
# AI tools require private API keys. 
# Create a class SecureClient that encapsulates an API token. Use Python's double underscore 
# prefix convention (__api_key) to make it a private attribute upon construction. Implement a 
# getter method called get_secure_masked_key() that returns only the first 4 characters followed by ****.

# Solution:

class SecureClient:
    def __init__(self, secret_key):
        self.__api_key = secret_key # Double underscore signals private variable
        
    def get_secure_masked_key(self):
        # Slice safely to avoid throwing errors if key is too short
        return f"{self.__api_key[:4]}****"

# Testing the implementation
client = SecureClient("sk-live987654321xyz")
print(client.get_secure_masked_key()) # Output: sk-l****
# print(client.__api_key) # This line would raise an AttributeError

# 8. Readable Logs: Overriding Dunder Methods 🟢 (Easy)
# Problem Statement:
# Printing objects directly yields unreadable memory pointers like <__main__.Agent object at 0x... >.
#  Create an Agent class that overrides the standard double-underscore string method __str__ so that 
# when passed directly into a print() statement, it explicitly outputs "Agent instance named: [name]".

# Solution:

class Agent:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        # Intercepts standard string formatting representation
        return f"Agent instance named: {self.name}"

# Testing the implementation
log_agent = Agent("Echo")
print(log_agent) 
# Output: Agent instance named: Echo


# 9. Custom Math: Arithmetic Dunder Overloading 🟡 (Medium)
# Problem Statement:
# If two independent agents work on a problem sequentially, we might want 
# to "add" their processing histories together. Build an AgentHistory class that 
# takes a list of strings called logs at initialization. Implement the __add__ dunder
#  method so that writing history1 + history2 creates and returns a brand-new AgentHistory 
# containing the combined lists.

# solution:

class AgentHistory:
    def __init__(self, logs):
        self.logs = logs
        
    def __add__(self, other):
        # Return a brand new instance of the same class type 
        combined_logs = self.logs + other.logs
        return AgentHistory(combined_logs)

# Testing the implementation
h1 = AgentHistory(["Started search", "Found matching files"])
h2 = AgentHistory(["Parsed items", "Finished task"])
h3 = h1 + h2
print(h3.logs)
# Output: ['Started search', 'Found matching files', 'Parsed items', 'Finished task']

# 10. Plugin Architecture: Polymorphism via Shared Interface 🟡 (Medium)
# Problem Statement:
# Agents interact with environments using varying tools (e.g., a Calculator tool or a
#  Web-Search tool). Demonstrate polymorphism by creating two different tool classes: 
# CalculatorTool and WebSearchTool. Ensure both implement a method with the exact same name:
#  call(query).CalculatorTool.call(query) returns "Calculating math for: [query]"WebSearchTool.call(query)
#  returns "Searching internet indices for: [query]"Write a standard Python function (outside the classes) 
# called use_plugin(tool_object, query) that runs the object's call method agnostic of its type.

# Solution:

class CalculatorTool:
    def call(self, query):
        return f"Calculating math for: {query}"

class WebSearchTool:
    def call(self, query):
        return f"Searching internet indices for: {query}"

# Polymorphic runner function accepting any class with a .call() interface
def use_plugin(tool_object, query):
    return tool_object.call(query)

# Testing the implementation
calc = CalculatorTool()
search = WebSearchTool()

print(use_plugin(calc, "5 + 5"))       # Output: Calculating math for: 5 + 5
print(use_plugin(search, "AI news"))   # Output: Searching internet indices for: AI news
