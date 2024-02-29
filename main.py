from tkinter import Tk, Canvas, Button, Scale, Label, HORIZONTAL
from random import choice
from math import pi, sin, cos

root = Tk()
root.title('Paintball')
root.wm_attributes('-topmost', 1)
root.resizable(0, 0)

width_window = 700
height_window = 700

canvas = Canvas(root, width=width_window, height=height_window, bg="gray")
canvas.pack()


# Screen cleaning
def clear_screen():
    canvas.delete('all')


# Draw a rectangle, arbitrary color with the selected slope level and size
def rendering(event):
    x, y = event.x, event.y
    print('{} {}'.format(x, y))
    colors = choice(['aquamarine', 'fuchsia', 'aqua', 'blue', 'red', 'green', 'orange',
                     'indigo', 'yellow', 'purple', 'pink', 'lime'])
    figure_size = slider_size.get()
    turn = slider_rotation.get() * pi / 180
    canvas.create_polygon(x - (figure_size * sin(60 * pi / 180 + turn)),
                          y + (figure_size * cos(60 * pi / 180 + turn)),
                          x - (figure_size * sin(-60 * pi / 180 + turn)),
                          y + (figure_size * cos(-60 * pi / 180 + turn)),
                          x - (figure_size * sin(-120 * pi / 180 + turn)),
                          y + (figure_size * cos(-120 * pi / 180 + turn)),
                          x - (figure_size * sin(120 * pi / 180 + turn)),
                          y + (figure_size * cos(120 * pi / 180 + turn)),
                          fill=colors, outline="black")


# Working field
canvas = Canvas(root, width=600, height=400, bg="white")
canvas.place(x=50, y=100)
canvas.bind('<Button-1>', rendering)

# Clear button
clear_button = Button(text='Clear', command=clear_screen, font=('Arial', 10, 'bold'))
clear_button.place(x=350, y=60)

# Slider adjusting the size of the figure
slider_size = Scale(root, from_=10, to_=100, length=200, orient=HORIZONTAL)
slider_size.place(x=250, y=520)
size_label = Label(root, text="Size", font=('Arial', 10, 'bold'))
size_label.place(x=190, y=540)

# Slider adjusting the angle of the figure
slider_rotation = Scale(root, from_=0, to_=360, length=200, orient=HORIZONTAL)
slider_rotation.place(x=250, y=570)
rotation_label = Label(root, text="Rotation", font=('Arial', 10, 'bold'))
rotation_label.place(x=180, y=590)

root.mainloop()
