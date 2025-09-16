import tkinter as tk

root = tk.Tk()
root.title("Label Example")

label = tk.Label(root, text="Hello, Manish!", font=("Arial", 18), fg="blue")
label.pack(pady=20)

root.mainloop()
