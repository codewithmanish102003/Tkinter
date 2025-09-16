import tkinter as tk

def greet():
    label.config(text="Welcome to Tkinter!")

root = tk.Tk()
root.title("Button Example")

label = tk.Label(root, text="Hello, Manish!", font=("Arial", 18), fg="blue")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", font=("Arial", 14), command=greet)
button.pack(pady=10)

root.mainloop()