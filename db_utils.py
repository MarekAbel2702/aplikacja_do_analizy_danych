from connection import connect_to_db

def add_order(user_id, product_id, quantity, order_date):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("EXEC AddOrder ?, ?, ?, ?", user_id, product_id, quantity, order_date)

        conn.commit()
        print("Zamówienie zostało dodane.")
    except Exception as e:
        print("Błąd dodawania zamówienia:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    add_order(1, 1, 5, '2025-04-09')