import tkinter as tk

root = tk.Tk()
root.title("Tkinter Variables Example")
root.geometry("300x200")

name_var = tk.StringVar()

def update_label():
    label.config(text=f"Hello, {name_var.get()}!")

entry = tk.Entry(root, textvariable=name_var)
entry.pack(pady=10)

button = tk.Button(root, text="Greet", command=update_label)
button.pack(pady=10)

label = tk.Label(root, text="Hello!")
label.pack(pady=10)

root.mainloop()
