import sqlite3
import pandas as pd

# 1. Establish our connection pipe
conn = sqlite3.connect("marketing_data.db")

# 2. Write a clean SQL query statement as a Python string
my_sql_query = """
SELECT keyword_text, search_volume 
FROM seo_keywords 
WHERE difficulty_score < 80.0
"""

print("🚁 Sending the Pandas Drone to fetch the data...")
# read_sql takes your query AND your connection pipe, doing all the hard work automatically
df_report = pd.read_sql(my_sql_query, conn)

# 3. Always close the connection pipe when finished
conn.close()

print("\n📊 Here is your clean Pandas DataFrame extracted directly via SQL:")
print(df_report)

# Now your students can use standard Pandas tools on it!
print(f"\n📈 Total potential traffic pool: {df_report['search_volume'].sum()}")
