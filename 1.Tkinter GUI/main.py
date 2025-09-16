import tkinter as tk

# Step 1: Create the main application window
root = tk.Tk()

# Step 2: Set window title and size
root.title("My First Tkinter App")
root.geometry("300x200")

# Step 3: Add a Label widget (text on the window)
label = tk.Label(root, text="Hello, Manish!", font=("Arial", 16))
label.pack(pady=20)

# Step 4: Run the application loop
root.mainloop()
