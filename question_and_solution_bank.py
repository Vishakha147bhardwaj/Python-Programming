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