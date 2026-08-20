import sqlite3
import pandas as pd

# Connect to the database
connection = sqlite3.connect("company_store.db")

# Pull the SQL data straight into a Pandas DataFrame
df = pd.read_sql("SELECT * FROM employees", connection)

# Look at your beautiful table
print(df)

connection.close()
