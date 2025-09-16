# Checkbutton Widget

import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("300x200")

checkbutton = tk.Checkbutton(root, text="Check me!", font=("Arial", 14))
checkbutton.pack(pady=20)

root.mainloop()
