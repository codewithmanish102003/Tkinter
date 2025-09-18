import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Example")

python_var = tk.BooleanVar()
js_var = tk.BooleanVar()

tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="JavaScript", variable=js_var).pack()

def show_choices():
    result = []
    if python_var.get(): result.append("Python")
    if js_var.get(): result.append("JavaScript")
    label.config(text="You selected: " + ", ".join(result))

tk.Button(root, text="Submit", command=show_choices).pack()
label = tk.Label(root, text="", font=("Arial", 14))
label.pack()

root.mainloop()
