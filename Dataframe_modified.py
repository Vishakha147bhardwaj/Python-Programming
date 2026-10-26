import pandas as pd
# Constructing a DataFrame from a dictionary of lists

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Peripherals'],
    'Price': [1200.00, 25.50, 300.00, 75.25],
    'Stock': [15, 120, 45, 80]
}
df = pd.DataFrame(data)

# print("\n--- Tabular DataFrame Grid ---")
# print(df)

# Structural inspection methods
# print("\n--- Metadata Summary (.info()) ---")
# df.info()  # Shows data types, row counts, and memory footprint

# print("\n--- First 2 Records (.head(2)) ---")
# print(df.head(2))

# Filter Condition: Must be Electronics AND must cost more than $50
# boolean_mask = (df['Category'] == 'Electronics') & (df['Price'] > 50)
# filtered_df = df[boolean_mask]

# print("--- Boolean Mask Output ---")
# print(filtered_df)

# Rewriting the complex filter as a human-readable expression string
# query_df = df.query("Category == 'Electronics' and Price > 50")

# print("\n--- String-Based .query() Output ---")
# print(query_df)

# Referencing standard local variables inside the expression string using '@'
# max_budget = 100
# budget_df = df.query("Price <= @max_budget")

# print("\n--- Dynamic Variable Query ---")
# print(budget_df)

# Expanded mock dataset for grouping operations
sales_data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'Rep': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Charlie'],
    'Sales':[250, 300, 150, 400, 200, 350],
    'Transactions': [42, 28, 55, 19, 31, 48]
}
sales_df = pd.DataFrame(sales_data)

# Basic Aggregation: Single column, single metric calculation
regional_sales = sales_df.groupby('Region')['Sales'].sum()

print("--- Basic Groupby Summary (Total Sales per Region) ---")
print(regional_sales)


# Dataset A: Core employee roster profiles
employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'name': ['John', 'Sarah', 'Mike', 'Emily'],
    'dept_id': [1, 2, 2, 9]  # Notice dept_id 9 does not exist in the departments table
})

# Dataset B: Official corporate department metadata
departments = pd.DataFrame({
    'dept_id': [1, 2, 3, 4],
    'dept_name': ['HR', 'Engineering', 'Marketing', 'Finance']  # Finance has no assigned employees
})

# 1. Inner Join: Strips out unmatched ids (drops employee 104 and depts 3 & 4)
# inner_merge = pd.merge(employees, departments, on='dept_id', how='inner')
# print("--- Inner Join Result ---")
# print(inner_merge)

# # 2. Left Join: Keeps all employees, even if their department doesn't exist
# left_merge = pd.merge(employees, departments, on='dept_id', how='left')
# print("\n--- Left Join Result ---")
# print(left_merge)

# # 3. Outer Join: Retains all structural information, filling gaps with NaN
# outer_merge = pd.merge(employees, departments, on='dept_id', how='outer')
# print("\n--- Outer Join Result ---")
# print(outer_merge)

# Production analytical data footprint destined for an AI Agent
agent_payload = pd.DataFrame({
    'task_id': ['T001', 'T002'],
    'status': ['pending', 'completed'],
    'priority': ['high', 'low']
})

# Standard raw export vs Token-optimized export
csv_string = agent_payload.to_csv(index=False)

print("--- Clean Token-Optimized CSV Output Stream ---")
print(csv_string)

# Record Orientation: Ideal for LLMs (Array of clear key-value objects)
json_records = agent_payload.to_json(orient='records', indent=2)
print("--- Agent-Ready Object Array (orient='records') ---")
print(json_records)

# Column Orientation: Grouped by structural column definitions
json_columns = agent_payload.to_json(orient='columns', indent=2)
print("\n--- Column-Oriented Serialization (orient='columns') ---")
print(json_columns)
