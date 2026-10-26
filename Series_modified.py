import pandas as pd

# Creating a Series with explicit labels
quantities = pd.Series([15, 24, 9], index=['apples', 'oranges', 'bananas'], name="inventory")

print("--- Series Representation ---")
print(quantities)

# How to pull the raw values or index markers out independently
print("\nExtracted Array Data:", quantities.values)
print("Extracted Index Labels:", quantities.index)
