import json

# A standard Python dictionary
data_dict = {"name": "Arjun", "verified": True, "hobbies": None}

# 1. Serialization: dict -> JSON string
json_string = json.dumps(data_dict, indent=4) 
print(json_string)
print(type(json_string))  # <class 'str'>
# Notice output changes: True becomes true, None becomes null, strings use double quotes

# 2. Deserialization: JSON string -> dict
parsed_dict = json.loads(json_string)
print(parsed_dict["name"]) # Output: Arjun
print(type(parsed_dict))   # <class 'dict'>
