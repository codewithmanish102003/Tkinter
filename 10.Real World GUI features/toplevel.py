import tkinter as tk
from tkinter import messagebox

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x200")
    
    tk.Label(settings_window, text="Change App Settings").pack(pady=10)
    tk.Button(settings_window, text="Close", command=settings_window.destroy).pack(pady=10)

root = tk.Tk()
root.title("Main App")
root.geometry("300x200")

tk.Button(root, text="Open Settings", command=open_settings).pack(pady=20)
root.mainloop()
