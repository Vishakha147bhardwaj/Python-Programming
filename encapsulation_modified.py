class SecurityPlugin:
    def __init__(self):
        self.public_status = "Active"          # Accessible anywhere
        self._protected_key = "Shared_Key_123" # Warning: Treat as private/internal
        self.__api_secret = "SuperSecret456"   # Strict Private (Triggers Name Mangling)

    # Getter method to read private data safely
    def get_secret(self):
        return f"Access Granted: {self.__api_secret}"

# Execution
plugin = SecurityPlugin()

print(plugin.public_status)   # Works perfectly: Output -> Active
print(plugin._protected_key)  # Works, but breaks Python conventions/best practices

# Testing strict privacy:
try:
    print(plugin.__api_secret) # Fails completely
except AttributeError:
    print("Error: Cannot access '__api_secret' directly from outside the class!")

# The proper way to access encapsulated data:
print(plugin.get_secret())    # Works: Output -> Access Granted: SuperSecret456
