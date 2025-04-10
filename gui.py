import customtkinter as ctk
from db_utils import get_user_total, add_order, connect_to_db
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplikacja Analizy Danych")
        self.geometry("800x600")

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill='both', expand=True, padx=10, pady=10)

        self.tab_add_order = self.tabview.add("Dodaj zamówienie")
        self.tab_user_total = self.tabview.add("Suma wydatków")
        self.tab_plot = self.tabview.add("Wykresy")

        self.build_add_order_tab()
        self.build_user_total_tab()
        self.build_plot_tab()

    def build_add_order_tab(self):
        ctk.CTkLabel(self.tab_add_order, text="Dodaj nowe zamówienie", font=("Arial", 18)).pack(pady=10)

        self.user_entry = ctk.CTkEntry(self.tab_add_order, placeholder_text="ID użytkownika")
        self.user_entry.pack(pady=5)

        self.product_entry = ctk.CTkEntry(self.tab_add_order, placeholder_text="ID produktu")
        self.product_entry.pack(pady=5)

        self.quantity_entry = ctk.CTkEntry(self.tab_add_order, placeholder_text="Ilość")
        self.quantity_entry.pack(pady=5)

        self.add_btn = ctk.CTkButton(self.tab_add_order, text="Dodaj zamówienie", command=self.gui_add_order)
        self.add_btn.pack(pady=10)

    def gui_add_order(self):
        try:
            uid = int(self.user_entry.get())
            pid = int(self.product_entry.get())
            qty = int(self.quantity_entry.get())
            add_order(uid, pid, qty,date.today().strftime("%Y-%m-%d"))
            messagebox.showinfo("Sukces, Zamówienie dodane")
        except Exception as e:
            messagebox.showerror(f"Błąd. Nie udało się dodać zamówienia:\n{e}")
    def build_user_total_tab(self):
        ctk.CTkLabel(self.tab_user_total,text="Sprawdź sumę wydatków", font=("Arial", 18)).pack(pady=10)

        self.user_total_entry = ctk.CTkEntry(self.tab_user_total, placeholder_text="ID użytkownika")
        self.user_total_entry.pack(pady=5)

        self.total_btn = ctk.CTkButton(self.tab_user_total, text="Pobierz sumę", command=self.gui_get_user_total)
        self.total_btn.pack(pady=10)

        self.total_result_label = ctk.CTkLabel(self.tab_user_total, text="", font=("Arial", 14))
        self.total_result_label.pack(pady=10)

    def gui_get_user_total(self):
        try:
            uid = int(self.user_total_entry.get())
            total = get_user_total(uid)
            if total:
                self.total_result_label.configure(text=f"Użytkownik {uid} wydał {total:.2f} zł")
            else:
                self.total_result_label.configure(text="Brak zamówień")
        except Exception as e:
            messagebox.showerror(f"Błąd pobierania sumy:\n{e}")

    def build_plot_tab(self):
        ctk.CTkLabel(self.tab_plot, text="Wybierz typ wykresu", font=("Arial", 18)).pack(pady=10)

        self.plot_buttons_frame = ctk.CTkFrame(self.tab_plot)
        self.plot_buttons_frame.pack(pady=5)

        ctk.CTkButton(self.plot_buttons_frame, text="Suma zamówień wg użytkowników",
                    command = self.plot_total_by_user).pack(padx=5, pady=5)

        ctk.CTkButton(self.plot_buttons_frame, text="Trend sprzedaży dzienny",
                      command=self.plot_sales_trend).pack(padx=5, pady=5)

        ctk.CTkButton(self.plot_buttons_frame, text="Kategorie produktów (udział %)",
                      command=self.plot_category_share).pack(padx=5, pady=5)

        self.plot_frame = ctk.CTkFrame(self.tab_plot)
        self.plot_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def plot_sales_trend(self):
        try:
            conn = connect_to_db()
            query = """
                SELECT OrderDate, SUM(p.Price * o.Quantity) AS Total
                FROM Orders o 
                JOIN Products p ON o.ProductID = p.ID
                GROUP BY OrderDate
                ORDER BY OrderDate
            """

            df = pd.read_sql(query, conn)
            conn.close()

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(df["OrderDate"], df["Total"], marker='o')
            ax.set_xlabel("Data")
            ax.set_ylabel("Łączna sprzedaż (zł)")
            ax.set_title("Trend dzienny sprzedaży")
            ax.grid(True)

            self._draw_plot(fig)
        except Exception as e:
            messagebox.showerror(f"Bład. Nie udało się wygenerować wykresu trendu:\n{e}")
    def plot_total_by_user(self):
        if not self.winfo_exists():
            return

        try:
            conn = connect_to_db()
            query = """
                SELECT u.Name, SUM(p.Price * o.Quantity) AS TotalSpent
                FROM Orders o
                JOIN Products p ON o.ProductID = p.ID
                JOIN Users u ON o.UserID = u.ID
                GROUP BY u.Name
                ORDER BY TotalSpent DESC
            """
            df = pd.read_sql(query, conn)
            conn.close()

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(df["Name"], df["TotalSpent"])
            ax.set_ylabel("Wydatki (zł)")
            ax.set_title("Suma zamówień wg użytkowników")
            ax.tick_params(axis='x', rotation=45)

            for widget in self.plot_frame.winfo_children():
                widget.pack_forget()

            if hasattr(self, "plot_canvas"):
                try:
                    self.plot_canvas.get_tk_widget().destroy()
                except Exception:
                    pass

            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

        except Exception as e:
            messagebox.showerror(f"Błąd. Nie udało się wygenerować wykresu:\n{e}")

    def plot_category_share(self):
        try:
            conn = connect_to_db()
            query = """
                SELECT p.Category, SUM(p.Price * o.Quantity) AS TotalValue
                FROM Orders o
                JOIN Products p ON o.ProductID = p.ID
                GROUP BY p.Category     
            """
            df = pd.read_sql(query, conn)
            conn.close()

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.pie(df["TotalValue"], labels=df["Category"], autopct='%1.1f%%', startangle=140)
            ax.set_title("Udział kategorii w sprzedaży")

            self._draw_plot(fig)

        except Exception as e:
            messagebox.showerror(f"Błąd. Nie udało się wygenerować wykresu udziałów:\n{e}")

    def _draw_plot(self, fig):
        try:
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
        except Exception:
            pass

        self.plot_canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)

if __name__ == "__main__":
    app = App()
    app.mainloop()