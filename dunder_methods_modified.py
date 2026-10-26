class PluginCollection:
    def __init__(self, items: list):
        self.items = items

    def __str__(self):
        """Controls what displays when you print() the object."""
        return f"Plugin Stack: {', '.join(self.items)}"

    def __len__(self):
        """Controls what displays when you run len() on the object."""
        return len(self.items)

    def __add__(self, other):
        """Controls what happens when you use the '+' operator to merge two objects."""
        return PluginCollection(self.items + other.items)

# Execution
stack_a = PluginCollection(["Compressor", "Blur"])
stack_b = PluginCollection(["Watermark"])

print(stack_a)          # Triggers __str__: Output -> Plugin Stack: Compressor, Blur
print(len(stack_a))     # Triggers __len__: Output -> 2

# Merging stacks using '+'
combined_stack = stack_a + stack_b  # Triggers __add__
print(combined_stack)   # Output -> Plugin Stack: Compressor, Blur, Watermark
