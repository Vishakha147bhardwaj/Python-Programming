import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS marketing_agency(
marketing_id INTEGER PRIMARY KEY,
price INTEGER,
brand TEXT
)
"""
)

cursor.executemany("INSERT INTO marketing_agency VALUES(?,?,?)",[
    (101,10000,'Nike'),
    (102,50000,'New Balances'),
    (103,100000,'Balancega')
])
connection.commit()

cursor.execute(
'''SELECT marketing_id, price,brand 
FROM marketing_agency
'''
)

result = cursor.fetchall()
for row in result:
    print(f'{row[0]}:{row[1]}:{row[2]}')

connection.close()