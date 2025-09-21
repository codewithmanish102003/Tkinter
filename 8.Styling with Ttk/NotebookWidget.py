import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Notebook Example")
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Frames for tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Home")
notebook.add(tab2, text="Settings")

# Add content
ttk.Label(tab1, text="Welcome to Home Tab").pack(pady=20)
ttk.Label(tab2, text="This is Settings Tab").pack(pady=20)

root.mainloop()
