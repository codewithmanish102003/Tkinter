import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Message Box Example")

def info_msg():
    messagebox.showinfo("Info", "This is an information message.")

def warn_msg():
    messagebox.showwarning("Warning", "This is a warning message!")

def error_msg():
    messagebox.showerror("Error", "Something went wrong.")

def confirm_exit():
    response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if response:  # True if Yes
        root.destroy()

tk.Button(root, text="Show Info", command=info_msg).pack(pady=5)
tk.Button(root, text="Show Warning", command=warn_msg).pack(pady=5)
tk.Button(root, text="Show Error", command=error_msg).pack(pady=5)
tk.Button(root, text="Exit", command=confirm_exit).pack(pady=5)

root.mainloop()
