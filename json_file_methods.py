import json

app_config = {"theme": "dark", "version": 2.1, "auto_update": False}

# 1. Writing data to a file
with open("config.json", "w") as file:
    json.dump(app_config, file, indent=4) # Directly saves into the file

# 2. Reading data from a file
with open("config.json", "r") as file:
    loaded_config = json.load(file)       # Parses file content into a dict
    print(loaded_config["theme"])         # Output: dark
