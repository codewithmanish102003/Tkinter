# Entry Widget(input field)

import tkinter as tk

root = tk.Tk()
root.title("Entry Example")
root.geometry("300x200")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=20)

root.mainloop()
