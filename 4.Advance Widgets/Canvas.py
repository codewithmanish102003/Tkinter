import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width=400, height=300, bg="lightblue")
canvas.pack()

# Draw line
canvas.create_line(10, 10, 200, 50, fill="red", width=3)

# Draw rectangle
canvas.create_rectangle(50, 80, 200, 150, fill="yellow")

# Draw oval (circle/ellipse)
canvas.create_oval(250, 80, 350, 180, fill="green")

# Draw polygon (triangle)
canvas.create_polygon(100, 200, 50, 250, 150, 250, fill="purple")

# Add text
canvas.create_text(200, 280, text="Tkinter Canvas Demo", font=("Arial", 14, "bold"))

root.mainloop()
