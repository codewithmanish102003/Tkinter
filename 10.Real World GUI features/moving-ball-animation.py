import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation")
root.geometry("400x300")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

ball = canvas.create_oval(10, 10, 50, 50, fill="red")
dx, dy = 3, 3
def move_ball():
    global dx, dy
    canvas.move(ball, dx, dy)
    pos = canvas.coords(ball)
    if pos[2] >= 400 or pos[0] <= 0:
        dx = -dx
    if pos[3] >= 300 or pos[1] <= 0:
        dy = -dy
    root.after(20, move_ball)  # repeat every 20ms

move_ball()
root.mainloop()
