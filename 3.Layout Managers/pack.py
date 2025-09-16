import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

tk.Label(root, text="Top", bg="lightblue").pack(side="top", fill="x")
tk.Label(root, text="Bottom", bg="lightgreen").pack(side="bottom", fill="x")
tk.Label(root, text="Left", bg="orange").pack(side="left", fill="y")
tk.Label(root, text="Right", bg="pink").pack(side="right", fill="y")

root.mainloop()
