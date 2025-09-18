import tkinter as tk

root = tk.Tk()
root.title("Simple Paint App")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill="black")

canvas.bind("<B1-Motion>", paint)  # Draw when mouse is dragged

root.mainloop()
