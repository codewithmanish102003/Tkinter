import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")

lang = tk.StringVar(value="None")

tk.Radiobutton(root, text="Frontend", variable=lang, value="Frontend").pack()
tk.Radiobutton(root, text="Backend", variable=lang, value="Backend").pack()
tk.Radiobutton(root, text="Fullstack", variable=lang, value="Fullstack").pack()

def show_selection():
    label.config(text=f"You selected: {lang.get()}")

tk.Button(root, text="Check", command=show_selection).pack()
label = tk.Label(root, text="", font=("Arial", 14))
label.pack()

root.mainloop()
