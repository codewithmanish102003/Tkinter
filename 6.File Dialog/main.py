import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("File Dialog Example")

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save File",
        defaultextension=".txt",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=5, pady=5)

# Create and pack buttons in the button frame
tk.Button(button_frame, text="Open File", command=open_file).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Save File", command=save_file).pack(side=tk.LEFT, padx=5)

# Create a frame for the text area with scrollbars
text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Add scrollbars
y_scroll = tk.Scrollbar(text_frame)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

x_scroll = tk.Scrollbar(text_frame, orient='horizontal')
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Create the text area
text_area = tk.Text(
    text_frame, 
    wrap=tk.NONE, 
    yscrollcommand=y_scroll.set,
    xscrollcommand=x_scroll.set,
    width=80, 
    height=20
)
text_area.pack(fill=tk.BOTH, expand=True)

# Configure the scrollbars
y_scroll.config(command=text_area.yview)
x_scroll.config(command=text_area.xview)

root.mainloop()
