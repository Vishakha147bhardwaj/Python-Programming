import sqlite3
import pandas as pd

# Connect to our agency database
connection = sqlite3.connect("agency.db")

# Define the SQL command we want to run
sql_query = "SELECT * FROM marketing_targets"

# Use Pandas to execute the query and format it instantly into a table grid
df_report = pd.read_sql(sql_query, connection)

# Close our line connection
connection.close()

# Display the beautiful result
print(df_report)
