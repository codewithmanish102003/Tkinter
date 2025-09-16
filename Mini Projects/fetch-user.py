import sqlite3

# Connect to DB
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Fetch all users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print results
print("Stored Users:")
for row in rows:
    print(f"Username: {row[0]}, Password: {row[1]}")

conn.close()
