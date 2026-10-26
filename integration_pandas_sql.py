import sqlite3
import pandas as pd

# ==========================================
# PART 1: NATIVE SQLITE3 WORKFLOW
# ==========================================

# 1. Connect to a database (creates 'company.db' if it doesn't exist)
conn = sqlite3.connect("company.db")

# 2. Create a cursor object to execute commands
cursor = conn.cursor()

# 3. Create a table using raw SQL
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
""")

# 4. Insert data using parameterized placeholders (?) to prevent SQL injection
employees_data = [
    ("Alice Smith", "Engineering", 85000),
    ("Bob Jones", "Marketing", 62000),
    ("Charlie Brown", "Engineering", 95000),
    ("Diana Prince", "HR", 71000)
]

cursor.executemany("""
    INSERT INTO employees (name, department, salary) 
    VALUES (?, ?, ?)
""", employees_data)

# 5. Commit changes to save them permanently to disk
conn.commit()

# 6. Run a SELECT query directly from the script
cursor.execute("SELECT * FROM employees WHERE department = 'Engineering'")
engineering_staff = cursor.fetchall()

print("--- Fetching via Native sqlite3 Cursor ---")
for row in engineering_staff:
    print(row)  # Outputs raw Python tuples


# ==========================================
# PART 2: PANDAS INTEGRATION
# ==========================================

print("\n--- Reading SQL directly into a Pandas DataFrame ---")
# Query the database and load the results straight into a DataFrame
query = "SELECT name, department, salary FROM employees WHERE salary > 70000"
df_high_earners = pd.read_sql(query, conn)

# Pandas formats the output into a clean, structured table view
print(df_high_earners)


print("\n--- Writing a Pandas DataFrame back to SQL ---")
# Create a brand new DataFrame out of thin air
new_data = {
    "name": ["Evan Wright", "Fiona Gallagher"],
    "department": ["Finance", "Finance"],
    "salary": [78000, 82000]
}
df_finance = pd.DataFrame(new_data)

# Export the DataFrame back to a completely new table inside company.db
# if_exists='append' ensures we add rows if the table already exists
df_finance.to_sql("employees", conn, if_exists="append", index=False)

# Verify the changes by printing the entire updated table
df_all_employees = pd.read_sql("SELECT * FROM employees", conn)
print(df_all_employees)


# ==========================================
# PART 3: CLEANUP
# ==========================================
# Always close the connection when your operations are finished
conn.close()
