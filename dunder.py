# class AIModel:
#     def __init__(self, model_name, version):
#         self.model_name = model_name
#         self.version = version

#     # Dunder method to change what print() shows
#     def __str__(self):
#         return f"AI Model: {self.model_name} (v{self.version})"

# my_ai = AIModel("GPT-4", "2.5")

# # Without __str__, print would show an ugly computer memory address
# print(my_ai)  # Output: AI Model: GPT-4 (v2.5)
# # print(my_ai.__str__())



class SmartDevice:
    def __init__(self, device_name, apps_installed):
        self.name = device_name
        self.apps = apps_installed # This will be a list of strings

    # Controls what happens when print() is used on this object
    def __str__(self):
        return f"SmartDevice: '{self.name}' running {len(self.apps)} apps."

    # Controls what happens when len() is used on this object
    def __len__(self):
        return len(self.apps)

# --- Deployment ---
my_phone = SmartDevice("AI-Phone 14", ["Gmail", "Maps", "ChatGPT"])

# Without __str__, this prints an ugly memory address. Now it prints clean text:
print(my_phone) 

# Automatically triggers the __len__ method behind the scenes:
print(f"Total apps: {len(my_phone)}") 
