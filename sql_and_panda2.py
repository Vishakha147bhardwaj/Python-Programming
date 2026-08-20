import sqlite3
import pandas as pd

# 1. Simulate data scraped by an AI agent into a Pandas DataFrame
scraped_data = {
    "product_name": ["Agentic Chatbot Pro", "SEO Optimizer Engine", "Content Bot 9000"],
    "competitor": ["TechCorp", "SEO_Masters", "AI_Write"],
    "monthly_price": [199.99, 49.00, 0.00]
}
agent_df = pd.DataFrame(scraped_data)

# 2. Open our connection vault
conn = sqlite3.connect("marketing_data.db")

print("📤 Exporting DataFrame into a permanent SQL table...")
# to_sql parameters explained to students:
# name = What to name the new SQL table
# con = The connection pipe variable
# if_exists = 'replace' means overwrite old data, 'append' means add to the bottom
# index = False drops the messy pandas row numbering from entering the clean database
agent_df.to_sql(name="competitor_products", con=conn, if_exists="replace", index=False)

print("✅ Data safely stored!")

# 3. Double-check by running a quick verification check
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM competitor_products")
row_count = cursor.fetchone()[0]
print(f"🗄️ Verification: There are now {row_count} rows sitting inside the SQL table!")

conn.close()
