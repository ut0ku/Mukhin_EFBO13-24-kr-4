import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Get table info
cursor.execute("PRAGMA table_info(products)")
columns = cursor.fetchall()

print("Table 'products' columns:")
for col in columns:
    print(f"  {col[1]}: {col[2]} (nullable: {col[3] == 0})")

conn.close()