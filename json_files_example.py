import json

app_config = {
    "theme": "Dark",
    "autoclose_timeout": 300,
    "user_preferences": {
        "notifications": True,
        "font_size": "Medium"
    }
}

# Writing the dictionary directly to a physical file
with open("config.json", "w", encoding="utf-8") as file:
    json.dump(app_config, file, indent=4)
    print("Configuration successfully saved to config.json!")

# Reading that exact file back into a separate Python variable
with open("config.json", "r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print(type(loaded_config))  # Output: <class 'dict'>
print(loaded_config["user_preferences"]["font_size"])  # Output: Medium
