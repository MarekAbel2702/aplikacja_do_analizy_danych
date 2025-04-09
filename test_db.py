from connection import connect_to_db

conn = connect_to_db()

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5 * FROM Users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)