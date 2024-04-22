import tkinter as tk

root = tk.Tk()
root.title("Graphic")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

outline_circle = canvas.create_oval(100, 100, 300, 300, outline="light green", width=3)

left_eye = canvas.create_oval(130, 150, 190, 210, fill="red")

right_eye = canvas.create_oval(210, 150, 270, 210, fill="blue")

smile = canvas.create_line(150, 240, 250, 240, fill="yellow", width=15)

triangle = canvas.create_polygon(200, 320, 160, 280, 240, 280, outline="black", fill="white", width=14)

root.mainloop()
