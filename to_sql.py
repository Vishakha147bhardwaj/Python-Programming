import sqlite3
import pandas as pd

new_data = {
    'name': ['Kabir', 'Riya'],
    'department': ['HR', 'Tech'],
    'salary': [55000, 75000]
}
df_new = pd.DataFrame(new_data)
connection = sqlite3.connect("company_store.db")

df_new.to_sql("new_hires", connection, if_exists="replace", index=False)

print("Data successfully exported to SQL!")
connection.close()
