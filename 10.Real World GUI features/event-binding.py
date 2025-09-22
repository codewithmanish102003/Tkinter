import tkinter as tk

def greet(event=None):
    print("Hello! Keyboard shortcut activated.")

root = tk.Tk()
root.title("Keyboard Shortcut Example")
root.geometry("300x150")

root.bind("<Return>", greet)   # Enter key
root.bind("<Escape>", lambda e: root.quit())  # Esc key to quit

tk.Label(root, text="Press Enter to Greet\nPress Esc to Exit").pack(pady=20)
root.mainloop()
