import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox Example")

ttk.Label(root, text="Select your country:").pack(pady=5)

countries = ["India", "USA", "UK", "Canada", "Germany"]
combo = ttk.Combobox(root, values=countries)
combo.set("India")  # default value
combo.pack(pady=5)

root.mainloop()
