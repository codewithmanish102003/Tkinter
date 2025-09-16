import tkinter as tk
from tkinter import messagebox
import sqlite3

# ------------------ Database Setup ------------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# ------------------ Register Function ------------------
def register_user():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == "" or pwd == "":
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (user, pwd))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    finally:
        conn.close()

# ------------------ Login Function ------------------
def login_user():
    user = entry_user.get()
    pwd = entry_pass.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Login Success", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# ------------------ Tkinter GUI ------------------
root = tk.Tk()
root.title("Login & Register System")
root.geometry("350x250")

# Username
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1, padx=10, pady=5)

# Password
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=5)

# Buttons
login_btn = tk.Button(root, text="Login", width=10, command=login_user)
login_btn.grid(row=2, column=0, pady=10)

register_btn = tk.Button(root, text="Register", width=10, command=register_user)
register_btn.grid(row=2, column=1, pady=10)

root.mainloop()
