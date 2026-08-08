# import json

# user_dict = {"name": "Alice", "is_admin": True, "balance": None}

# # Serialize into a raw JSON string
# json_string = json.dumps(user_dict)
# print(json_string)  
# # Output: {"name": "Alice", "is_admin": true, "balance": null}

# # Pretty-print with indentation for better readability
# pretty_json = json.dumps(user_dict, indent=4)

# import json

# raw_json = '{"name": "Bob", "is_admin": false, "hobbies": ["coding", "chess"]}'

# # Deserialize JSON string into a Python dict
# parsed_dict = json.loads(raw_json)
# print(type(raw_json))
# print(type(parsed_dict))
# # print(parsed_dict['name']) 

# import json

# setting = {"theme": "dark", "volume": 90}

# with open("config.json", "w") as file:
#     json.dump(setting, file, indent=4) 

# import json

# with open("config.json", "r") as file:
#     loaded_settings = json.load(file)

# print(loaded_settings["volume"])  
student = {"name": "Alice", "age": 20}
print(student.get("grade", "N/A"))