import sqlite3

conn = sqlite3.connect("userdb.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS account (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    accno TEXT NOT NULL UNIQUE,
    ifsc TEXT NOT NULL,
    branch_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")

conn.commit()
conn.close()

print("Table ensured.")
