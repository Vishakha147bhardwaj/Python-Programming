class SecretAgent:
    def __init__(self, name, encryption_key):
        self.name = name
        self.__encryption_key = encryption_key  

   
    def get_key(self, password):
        if password == "Admin123":
            return self.__encryption_key
        return "Access Denied!"

agent = SecretAgent("James", "XYZ-999")


# print(agent.__encryption_key) 

print(agent.get_key("WrongPass"))  
# print(agent.get_key("Admin123"))   