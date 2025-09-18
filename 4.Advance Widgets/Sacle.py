import tkinter as tk

root = tk.Tk()
root.title("Scale Example")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack(pady=10)

def show_value():
    label.config(text=f"Value: {scale.get()}")

tk.Button(root, text="Get Value", command=show_value).pack()
label = tk.Label(root, text="", font=("Arial", 14))
label.pack()

root.mainloop()
