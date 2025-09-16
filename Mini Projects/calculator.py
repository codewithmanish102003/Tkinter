import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Mini Calculator")

entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 4)
]

for btn in buttons:
    if len(btn) == 3:
        text, row, col = btn
        b = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2)
        b.grid(row=row, column=col, padx=5, pady=5)
        b.bind("<Button-1>", click)
    else:  # "=" button spans across columns
        text, row, col, colspan = btn
        b = tk.Button(root, text=text, font=("Arial", 18), width=22, height=2, bg="lightblue")
        b.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()
