from connection import connect_to_db

def add_order(user_id, product_id, quantity, order_date):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("EXEC AddOrder ?, ?, ?, ?", (user_id, product_id, quantity, order_date))

        conn.commit()
        print("Zamówienie zostało dodane.")
    except Exception as e:
        print("Błąd dodawania zamówienia:", e)
    finally:
        conn.close()

def get_user_total(user_id):
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("EXEC GetUserOrderTotal ?", (user_id,))
        result = cursor.fetchone()
        if result and result[0] is not None:
            return result[0]
        else:
            return None
    except Exception as e:
        print("Błąd podczas pobierania sumy zamówień:", e)
        return None
    finally:
        conn.close()

if __name__ == "__main__":
    add_order(1, 1, 5, '2025-04-09')

    total = get_user_total(1)
    if total:
        print(f"Użytkownik 1 wydał: {total:.2f} zł")
    else:
        print("Brak danych o zamówieniach dla użytkownika.")