# Frame Widget

import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("300x200")

frame = tk.Frame(root, bg="blue", width=200, height=100)
frame.pack(pady=20)

root.mainloop()