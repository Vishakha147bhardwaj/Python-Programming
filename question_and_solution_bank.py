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


# 🌐 Topic 1: Working with APIs & Web ScrapingQuestion 
# 1: Scraping and Filtering Items
# Problem Statement:
# Write a function get_highly_rated_books(url) using requests and BeautifulSoup.
#  Parse the given URL to find all book elements (<article class="book_pod">). 
# Extract and return a list of titles of books that have a class of either "star-rating Four"
#  or "star-rating Five".

# Solution:
import requests
from bs4 import BeautifulSoup

def get_highly_rated_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = []
    # Find all book article elements
    books = soup.find_all('article', class_='book_pod')
    
    for book in books:
        # Check if the star-rating class matches Four or Five
        if book.find(class_='star-rating Four') or book.find(class_='star-rating Five'):
            # Extract title from the anchor tag inside the h3 element
            title = book.h3.a['title']
            titles.append(title)
            
    return titles


# Question 2: Multi-Page Scraping with CSS Selectors
# Problem Statement:
# Write a Python script that uses a CSS selector (select()) to scrape text from all paragraphs
#  (p.content) across the first 3 pages of a paginated blog. The base URL structure is https://example-blog.com. 
# Return all extracted paragraphs in a single flat list.

# Solution:
import requests
from bs4 import BeautifulSoup

def scrape_blog_paragraphs(base_url):
    all_paragraphs = []
    
    for page in range(1, 4):
        response = requests.get(f"{base_url}{page}")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Use CSS selector to extract matching paragraph structures
        elements = soup.select('p.content')
        for el in elements:
            all_paragraphs.append(el.get_text())
            
    return all_paragraphs

# Question 3: Authenticated POST Request with Error Handling
# Problem Statement:Write a function submit_agent_payload(api_url, token, payload) that 
# sends a POST request to an API endpoint. Pass the token inside the HTTP headers as 
# {"Authorization": f"Bearer {token}"} and send the payload data as JSON. 
# If the response status code is not 201, raise a RuntimeError displaying the status code received.

# Solution:
import requests

def submit_agent_payload(api_url, token, payload):
    headers = {"Authorization": f"Bearer {token}"}
    
    # Send POST request converting payload payload to JSON automatically
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code != 201:
        raise RuntimeError(f"Failed submission. Status code received: {response.status_code}")
        
    return response.json()

# Question 4: URL Parameter Configuration
# Problem Statement:
# Write a script using the requests library to fetch data from https://weather.com. 
# Configure the request dynamically using the params dictionary argument to pass the 
# following key-value pairs: location="Delhi", units="metric", and limit=5. Return the 
# raw JSON payload response.

# Solution:

import requests

def fetch_weather_data():
    url = "https://weather.com"
    query_params = {
        "location": "Delhi",
        "units": "metric",
        "limit": 5
    }
    
    response = requests.get(url, params=query_params)
    return response.json()



# Question 5: Programmatic Robots.txt Compliance Check
# Problem Statement:
# Write a Python function is_scraping_allowed(url, user_agent="*") using Python's built-in urllib.
# robotparser. The function must read the robots.txt file located at the domain root of the input
#  URL and return a boolean indicating whether the specified User-Agent is permitted to scrape that path.

# Solution:
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

def is_scraping_allowed(url, user_agent="*"):
    parsed_url = urlparse(url)
    # Reconstruct base scheme and network location root for robots.txt positioning
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    
    return rp.can_fetch(user_agent, url)


# 🧵 Topic 2: Strings & String Methods
# Question 6: Parsing and Rebuilding Log Data
# Problem Statement:
# You are given a raw log string: "[ERROR] :: 2026-09-01 :: Connection failed  \n". 
# Write a function clean_and_split_log(log_str) that strips whitespace, splits the 
# log by the :: delimiter, removes empty padding from each token, and returns a tuple 
# in the format: (status, date, message).

# Solution:
def clean_and_split_log(log_str):
    # Strip leading/trailing whitespaces and newlines
    cleaned = log_str.strip()
    # Split tokens strictly by the double colon identifier
    tokens = cleaned.split("::")
    # Clean whitespace padding out of individual extracted sub-strings
    final_tokens = [token.strip() for token in tokens]
    
    return (final_tokens[0], final_tokens[1], final_tokens[2])


# Question 7: Dynamic Few-Shot Prompt Template
# Problem Statement:
# Write a function generate_few_shot_prompt(examples, system_role) where examples is a
#  list of tuples containing user/assistant pairs (e.g., [("Hi", "Hello"), ("Bye", "Goodbye")]).
#  Use f-strings and .join() to construct a single string block formatted exactly as a chat model
#  prompt container, appending the system_role at the top.

# Solution:
def generate_few_shot_prompt(examples, system_role):
    # Map raw examples list to consistent layout formatting structures
    formatted_examples = [
        f"User: {pair[0]}\nAssistant: {pair[1]}" for pair in examples
    ]
    # Build text block dynamically using string joins
    examples_block = "\n---\n".join(formatted_examples)
    
    return f"System: {system_role}\n\nExamples:\n{examples_block}"


# Question 8: Anonymizing Private Entities
# Problem Statement:
# Write a function redact_api_keys(prompt_text) that finds instances of keys structured 
# as "sk-proj-" followed by 8 alphanumeric characters (e.g., sk-proj-abc123xyz). 
# Replace the entire sequence with the string "[[REDACTED]]" programmatically using
#  structural string operations or string slicing methods.

# Solution:
def redact_api_keys(prompt_text):
    while "sk-proj-" in prompt_text:
        idx = prompt_text.find("sk-proj-")
        # Extract target window slice boundaries (prefix + 8 characters)
        target_slice = prompt_text[idx:idx + 16]
        prompt_text = prompt_text.replace(target_slice, "[[REDACTED]]")
        
    return prompt_text

# Question 9: Structural CSV Line Transformer
# Problem Statement:
# Write a function transform_csv_row(csv_line) that takes a single comma-separated text string representing
#  a row (e.g., "agent_01,  active ,gpt-4 "). Clean up individual item padding using string mutations, 
# replace instances of "gpt-4" with "gpt-4o", and join the elements back together using a pipe delimiter (|) 
# instead of a comma.

# Solution:
def transform_csv_row(csv_line):
    # Split text line by default comma separations
    elements = csv_line.split(",")
    # Strip individual string element boundaries
    cleaned_elements = [el.strip() for el in elements]
    
    # Process modifications on targets inside collection elements list
    transformed = [
        "gpt-4o" if item == "gpt-4" else item for item in cleaned_elements
    ]
    
    # Pack items together using modern pipe sequence character
    return "|".join(transformed)


# Question 10: Dynamic JSON-Prompt Builder
# Problem Statement:
# Given a string template representing a structured JSON prompt: "{'task': '{task_name}', 'temperature': {temp}}"
#  and a multi-line code string. Write a Python snippet that safely formats the template using explicit variable 
# injection, doubling necessary structural brackets so it returns a valid JSON-like prompt string without triggering
#  a KeyError.

# Solution:
def build_json_prompt(task_name, temp):
    # Escape structural dictionary literal curly brackets by doubling them up
    template = "{{'task': '{task_name}', 'temperature': {temp}}}"
    
    # Inject variables dynamically into parameters safely
    return template.format(task_name=task_name, temp=temp)
