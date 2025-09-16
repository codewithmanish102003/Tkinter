# Radio Button Widget

import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

radio = tk.Radiobutton(root, text="Radio me!", font=("Arial", 14))
radio.pack(pady=20)

root.mainloop()
