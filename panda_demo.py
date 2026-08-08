import pandas as pd
ages = pd.Series([25, 30, 35], name="Age")
print("--- This is a Series (Single Column) ---")
print(ages)
print()

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data)
print("--- This is a DataFrame (Full Spreadsheet) ---")
print(df)

