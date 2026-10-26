import json

# This is a raw text string representing JSON data coming from an API or AI tool
# Note the strict use of double quotes inside the string!
ai_response_json = """
{
    "tool_used": "web_search",
    "success": true,
    "results_found": 3,
    "meta": {
        "latency_ms": 142
    }
}
"""

# 1. DESERIALIZATION: Convert raw JSON string into a Python Dictionary
data_dict = json.loads(ai_response_json)

print(type(data_dict))  # Output: <class 'dict'>
print(data_dict["meta"]["latency_ms"])  # Output: 142
# Notice how JSON's lowercase 'true' became Python's capitalized 'True' automatically
print(data_dict["success"])  # Output: True


# 2. SERIALIZATION: Convert a Python Dictionary back into a clean JSON string
# The 'indent' parameter makes the string human-readable (pretty-printing)
new_json_string = json.dumps(data_dict, indent=4)

print(new_json_string)
# Output will look exactly like a cleanly formatted block of text
