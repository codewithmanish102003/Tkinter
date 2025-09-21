import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# --------------------------
# Notepad Application
# --------------------------

def new_file():
    text_area.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
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
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to quit?"):
        root.destroy()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def about_app():
    messagebox.showinfo("About Notepad", "Tkinter Notepad\nCreated by Manish 🚀")

# --------------------------
# Main Window
# --------------------------
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 10), padding=5)

# --------------------------
# Text Area with Scrollbar
# --------------------------
text_area = tk.Text(root, wrap="word", undo=True, font=("Consolas", 12))
text_area.pack(expand=True, fill="both")

scrollbar = ttk.Scrollbar(text_area)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# --------------------------
# Menu Bar
# --------------------------
menubar = tk.Menu(root)
root.config(menu=menubar)

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Help Menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_app)

# --------------------------
# Run App
# --------------------------
root.mainloop()
