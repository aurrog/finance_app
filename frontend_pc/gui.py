import tkinter as tk
from tkinter import ttk
import requests
from settings import *  # Предполагается, что у тебя есть файл settings.py с TYPE_COLORS


def get_transactions():
    response = requests.get('http://127.0.0.1:5000/transactions')
    if response.status_code == 200:
        transactions = response.json()
        return transactions
    else:
        print('Ошибка при выполнении запроса GET')
        return []


def load_transactions():
    data = get_transactions()

    for transaction in data:
        transaction_id, transaction_type, amount, description, date = transaction

        # Создаем Frame для каждой транзакции
        transaction_frame = ttk.Frame(frame)
        transaction_frame.pack(fill='x', pady=5)

        # Кнопка с amount
        amount_button = tk.Button(
            transaction_frame,
            text=f"{amount} ₽",
            bg=TYPE_COLORS[transaction_type],
            fg="white",
            font=('Arial', 25),
            anchor='w',
            bd=0,
            highlightthickness=0
        )
        amount_button.pack(side='left', fill='x', expand=True)

        # Лейбл с датой
        date_label = tk.Label(
            transaction_frame,
            text=date,
            bg="#f0f0f0",
            fg="gray",
            font=('Arial', 12)
        )
        date_label.pack(side='right', padx=10)


root = tk.Tk()
root.title("Finance app")
root.geometry('500x600')

canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw", width=500)

load_transactions()


def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


canvas.bind_all("<MouseWheel>", on_mousewheel)

root.mainloop()
