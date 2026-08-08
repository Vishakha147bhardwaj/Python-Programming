import pandas as pd
import sqlite3

# 1. This simulates a data grid your team collected inside Python
new_keywords_grid = {
    "target_id":[101,202],
    "keyword_text": ["cheap wireless earbuds", "organic coffee beans"],
    "monthly_volume": [8000, 1200]
}
df_new_data = pd.DataFrame(new_keywords_grid)

# 2. Open our connection line to the database
connection = sqlite3.connect("agency.db")

# 3. Dump the entire grid into a SQL database table called 'marketing_targets'
df_new_data.to_sql(
    name="marketing_targets", 
    con=connection, 
    if_exists="append", 
    index=False
)
connection.close()

print("Entire data grid successfully pushed to the SQL database!")

