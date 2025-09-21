import tkinter as tk
from tkinter import ttk, messagebox
import os
from datetime import datetime

# --------------------------
# Expense Tracker Functions
# --------------------------
expenses = []

def load_expenses():
    """Load saved expenses from file"""
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    expenses.append(parts)
                    expense_table.insert("", tk.END, values=parts)
        update_total()

def save_expenses():
    """Save expenses to file"""
    with open("expenses.txt", "w", encoding="utf-8") as f:
        for exp in expenses:
            f.write("|".join(exp) + "\n")

def add_expense():
    date = date_entry.get().strip()
    category = category_entry.get().strip()
    amount = amount_entry.get().strip()
    note = note_entry.get().strip()

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    if category and amount.isdigit():
        exp = [date, category, amount, note]
        expenses.append(exp)
        expense_table.insert("", tk.END, values=exp)

        save_expenses()
        update_total()

        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter Category and a valid Amount!")

def delete_expense():
    selected = expense_table.selection()
    if selected:
        index = expense_table.index(selected[0])
        expenses.pop(index)
        expense_table.delete(selected[0])
        save_expenses()
        update_total()
    else:
        messagebox.showwarning("Delete Error", "Please select an expense to delete.")

def update_total():
    total = sum(int(exp[2]) for exp in expenses)
    total_label.config(text=f"Total Expense: ₹{total}")

# --------------------------
# Main Window
# --------------------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x500")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
style.configure("Treeview", font=("Arial", 10), rowheight=25)

# --------------------------
# Input Frame
# --------------------------
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
date_entry = ttk.Entry(frame, width=15)
date_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Category:").grid(row=0, column=2, padx=5, pady=5)
category_entry = ttk.Entry(frame, width=15)
category_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame, text="Amount:").grid(row=0, column=4, padx=5, pady=5)
amount_entry = ttk.Entry(frame, width=10)
amount_entry.grid(row=0, column=5, padx=5, pady=5)

ttk.Label(frame, text="Note:").grid(row=0, column=6, padx=5, pady=5)
note_entry = ttk.Entry(frame, width=20)
note_entry.grid(row=0, column=7, padx=5, pady=5)

ttk.Button(frame, text="Add Expense", command=add_expense).grid(row=0, column=8, padx=5, pady=5)

# --------------------------
# Expense Table
# --------------------------
table_frame = ttk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("Date", "Category", "Amount", "Note")
expense_table = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    expense_table.heading(col, text=col)
    expense_table.column(col, anchor="center")

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=expense_table.yview)
expense_table.configure(yscrollcommand=scrollbar.set)

expense_table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --------------------------
# Delete Button & Total
# --------------------------
ttk.Button(root, text="Delete Expense", command=delete_expense).pack(pady=5)
total_label = ttk.Label(root, text="Total Expense: ₹0", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

# --------------------------
# Load Data on Startup
# --------------------------
load_expenses()

# --------------------------
# Run App
# --------------------------
root.mainloop()
