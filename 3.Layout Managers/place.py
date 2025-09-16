import tkinter as tk

root = tk.Tk()
root.title("Place Example")
root.geometry("300x200")

tk.Label(root, text="Exact Position", bg="yellow").place(x=100, y=80)
tk.Button(root, text="Click Me").place(x=120, y=120)

root.mainloop()
