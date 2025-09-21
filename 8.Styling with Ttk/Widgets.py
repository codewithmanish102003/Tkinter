import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk Example")

ttk.Label(root, text="Username:").pack(pady=5)
ttk.Entry(root).pack(pady=5)

ttk.Label(root, text="Password:").pack(pady=5)
ttk.Entry(root, show="*").pack(pady=5)

ttk.Button(root, text="Login").pack(pady=10)

root.mainloop()
