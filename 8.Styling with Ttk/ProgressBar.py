import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Progressbar Example")

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

progress["maximum"] = 100
progress["value"] = 40  # current progress

root.mainloop()
