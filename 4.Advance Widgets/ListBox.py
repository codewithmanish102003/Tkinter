import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")

listbox = tk.Listbox(root, font=("Arial", 14))
listbox.pack(pady=10)

items = ["Python", "JavaScript", "C++", "Java", "Django", "React"]
for item in items:
    listbox.insert(tk.END, item)

def show_selected():
    selection = listbox.get(tk.ACTIVE)
    label.config(text=f"Selected: {selection}")

btn = tk.Button(root, text="Select", command=show_selected)
btn.pack()

label = tk.Label(root, text="", font=("Arial", 14))
label.pack()

root.mainloop()
