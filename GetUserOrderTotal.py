from connection import connect_to_db

def get_user_total(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("EXEC GetUserOrderTotal ?", user_id)
    result = cursor.fetchone()
    if result:
        print(f"Użytkownik {user_id} wydał: {result[0]} zł")
    else:
        print("Brak danych.")

if __name__ == "__main__":
    get_user_total(user_id=5)