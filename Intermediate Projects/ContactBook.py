import tkinter as tk
from tkinter import ttk, messagebox
import os

# --------------------------
# Contact Book Functions
# --------------------------
contacts = []

def load_contacts():
    """Load contacts from file on startup"""
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r", encoding="utf-8") as f:
            for line in f:
                contacts.append(line.strip())
                contact_list.insert(tk.END, line.strip())

def save_contacts():
    """Save all contacts to file"""
    with open("contacts.txt", "w", encoding="utf-8") as f:
        for contact in contacts:
            f.write(contact + "\n")

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()

    if name and phone:
        contact = f"{name} | {phone} | {email}"
        contacts.append(contact)
        contact_list.insert(tk.END, contact)

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        save_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        contact_list.delete(index)
        save_contacts()
    else:
        messagebox.showwarning("Delete Error", "Please select a contact to delete.")

# --------------------------
# Main Window
# --------------------------
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 10), padding=5)

# --------------------------
# Input Frame
# --------------------------
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_entry = ttk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Phone:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
phone_entry = ttk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
email_entry = ttk.Entry(frame, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Button(frame, text="Add Contact", command=add_contact).grid(row=3, column=1, sticky="e", pady=10)

# --------------------------
# Contact List
# --------------------------
contact_list = tk.Listbox(root, font=("Arial", 12))
contact_list.pack(fill="both", expand=True, padx=10, pady=10)

ttk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# --------------------------
# Load Existing Contacts
# --------------------------
load_contacts()

# --------------------------
# Run App
# --------------------------
root.mainloop()
