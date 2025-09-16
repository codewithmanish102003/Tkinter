import tkinter as tk
from tkinter import messagebox

def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == "admin" and pwd == "1234":
        messagebox.showinfo("Login Success", "Welcome, Manish!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Username
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1, padx=10, pady=5)

# Password
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=5)

# Button
login_btn = tk.Button(root, text="Login", command=login)
login_btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
