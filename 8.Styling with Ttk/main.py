import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk Style Example")

style = ttk.Style()
style.theme_use("clam")  # themes: clam, default, alt, classic

style.configure("TButton",
                font=("Arial", 12, "bold"),
                foreground="blue",
                padding=10)

ttk.Button(root, text="Styled Button").pack(pady=20)

root.mainloop()
