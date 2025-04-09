import pyodbc

def connect_to_db():
    conn_str = (
        "Driver={SQL Server};Server=LAPTOP-M79Q5NVL\\SQLEXPRESS;Database=Aplikacja_Analizy_Danych;"
        "Trusted_Connection=yes"
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("Połączono z bazą danych")
        return conn
    except Exception as e:
        print("Błąd połączenia:", e)
        return None

if __name__ == "__main__":
    connect_to_db()