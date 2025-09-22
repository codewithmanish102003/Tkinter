import customtkinter as ctk

root = ctk.CTk()
root.geometry("300x200")
root.title("CustomTkinter Example")

button = ctk.CTkButton(root, text="Click Me", fg_color="#4CAF50")
button.pack(pady=50)

root.mainloop()
