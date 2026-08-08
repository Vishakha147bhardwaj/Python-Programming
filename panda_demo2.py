import pandas as pd

sales_data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Department": ["Sales", "Marketing", "Sales", "Sales", "Marketing"],
    "Revenue": [5000, 7000, 6000, 3000, 8000]
}

df_sales = pd.DataFrame(sales_data)
print(df_sales)

# --- 1. FILTERING ---
# Only keep departments that are 'Sales'
sales_only = df_sales[df_sales["Department"] == "Sales"]
print("--- Filtered Data (Sales Only) ---")
print(sales_only)
print()

# --- 2. GROUPBY ---
# Group by Department and sum up their total revenue
dept_totals = df_sales.groupby("Department")["Revenue"].sum().reset_index()
print("--- Grouped Data (Total Revenue by Dept) ---")
print(dept_totals)
print()

# # --- 3. MERGE ---
# Separate table with Employee details
emp_details = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"]
}
df_employees = pd.DataFrame(emp_details)

# Glue the sales table and employee table together using Employee_ID
merged_df = pd.merge(df_sales, df_employees, on="Employee_ID")
print("--- Merged Data (Sales joined with Names) ---")
print(merged_df)

merged_df.to_csv("final_report.csv", index=False)
print("Successfully saved final_report.csv!")

merged_df.to_json("agent_feed.json", orient="records", indent=4)
print("Successfully saved agent_feed.json!")
