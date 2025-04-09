import customtkinter as ctk
from db_utils import get_user_total, add_order
from datetime import date

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplikacja Analizy Danych")
        self.geometry("600x400")

        self.title_label = ctk.CTkLabel(self, text="Witaj w aplikacji", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=20)

        self.user_id_entry = ctk.CTkEntry(self, placeholder_text="ID użykownika")
        self.user_id_entry.pack(pady=5)

        self.check_btn = ctk.CTkButton(self, text="Sprawdź wydatki", command=self.show_user_total)
        self.check_btn.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)

        self.add_order_btn = ctk.CTkButton(self, text="Dodaj testowe zamówienie", command=self.add_test_order)
        self.add_order_btn.pack(pady=20)

    def show_user_total(self):
        try:
            user_id = int(self.user_id_entry.get())
            result = get_user_total(user_id)
            if result:
                self.result_label.configure(text=f"Użytkownik {user_id} wydał: {result:.2f} zł")
            else:
                self.result_label.configure(text="Brak danych dla tego użytkownika.")
        except ValueError:
            self.result_label.configure(text="Podaj poprawne ID (liczba całkowita)")

    def add_test_order(self):
        add_order(1, 1, 1, '2025-04-09')
        self.result_label.configure(text="Dodano testowe zamówienie.")

if __name__ == "__main__":
    app = App()
    app.mainloop()