import turtle
import random

def draw_spiral_pattern():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set the background color
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.width(2)  # Set pen width

    colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan"]  # Predefined color list

    for i in range(180):  # Number of iterations to create the spiral
        t.pencolor(random.choice(colors))  # Randomly pick a color from the list
        t.forward(i * 2)  # Increase the step size as the spiral grows
        t.left(59)  # Change angle to create the spiral effect
        t.forward(i * 2)
        t.left(59)

    screen.mainloop()  # Keeps the window open

if __name__ == "__main__":
    draw_spiral_pattern()
