import tkinter as tk

# ----------- Functions -----------
def click(event=None):
    text = event.widget.cget("text") if event else None
    if event:  # clicked by button
        handle_input(text)
    else:      # typed by keyboard
        handle_input(entry.get()[-1])  

def handle_input(text):
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
    elif text == "MC":  # Memory Clear
        memory.set(0)
    elif text == "MR":  # Memory Recall
        entry.insert(tk.END, str(memory.get()))
    elif text == "M+":  # Memory Add
        try:
            memory.set(memory.get() + float(entry.get()))
        except:
            entry.insert(tk.END, "Error")
    elif text == "M-":  # Memory Subtract
        try:
            memory.set(memory.get() - float(entry.get()))
        except:
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

def key_input(event):
    if event.char.isdigit() or event.char in "+-*/.":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        handle_input("=")
    elif event.keysym == "BackSpace":
        current = entry.get()[:-1]
        entry.delete(0, tk.END)
        entry.insert(tk.END, current)

# ----------- Main Window -----------
root = tk.Tk()
root.title("Advanced Calculator")

memory = tk.DoubleVar(value=0)

entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("MC", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("MR", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("M+", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3), ("M-", 4, 4),
    ("=", 5, 0, 5)
]

for btn in buttons:
    if len(btn) == 3:
        text, row, col = btn
        b = tk.Button(root, text=text, font=("Arial", 16), width=5, height=2)
        b.grid(row=row, column=col, padx=5, pady=5)
        b.bind("<Button-1>", click)
    else:  # "=" button spanning columns
        text, row, col, colspan = btn
        b = tk.Button(root, text=text, font=("Arial", 16), width=35, height=2, bg="lightblue")
        b.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
        b.bind("<Button-1>", click)

# Bind keyboard input
root.bind("<Key>", key_input)

root.mainloop()
