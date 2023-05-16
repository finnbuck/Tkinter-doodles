import math
import tkinter as tk
import random

# Create the main window
window = tk.Tk()

# Create a canvas widget
canvas = tk.Canvas(window, width=1200, height=1200, background="#FFFFFF")
canvas.pack()

#coloring = [
#    [2, 1, 2, 1, 1],
#    [2, 2, 1, 1, 1],
#    [2, 0, 2, 0, 0],
#    [2, 2, 0, 0, 0],
#    [2, 2, 1, 1, 0],
#    [2, 2, 1, 0, 1],
#    [2, 0, 2, 1, 1],
#    [1, 2, 1, 2, 0],
#    [2, 2, 0, 0, 1],
#    [2, 2, 0, 1, 0],
#    [2, 1, 2, 0, 0],
#    [0, 2, 0, 2, 1]
#]

#coloring = [
#    [2, 1, 1, 1, 1],
#    [2, 1, 1, 1, 0],
#    [2, 1, 1, 0, 1],
#    [2, 1, 1, 0, 0],
#    [2, 1, 0, 1, 0],
#    [2, 1, 0, 0, 1],
#    [2, 0, 1, 1, 0],
#    [2, 1, 0, 0, 0],
#    [2, 0, 1, 0, 0],
#    [2, 0, 0, 0, 0]
#]

coloring = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def populate():

    #start_x = 100
    #start_y = 50



    id_number = 0
    for i in range(4):
        for j in range(2):
            center_x, center_y = 100+i*200, 100+j*200
            radius = 60
            canvas.create_oval(center_x-radius, center_y-radius, center_x+radius, center_y+radius, width=5)
            drawCircle(center_x, center_y, id_number)
            id_number += 1


# Define a callback function that gets the width of the canvas
def drawCircle(center_x, center_y, id_number):

    bigRadius = 60
    smallRadius = 20

    colors = ["white", "grey", "black"]

    # Set the number of circles
    num_circles = 5

    # Set the starting angle
    angle = 0

    # Set the angle increment
    angle_increment = 2 * math.pi / num_circles

    for i in range(num_circles):
        # Calculate the x and y coordinates of the center of the circle
        x = center_x + bigRadius * math.cos(angle)
        y = center_y + bigRadius * math.sin(angle)

        # Draw the circle
        canvas.create_oval(x-smallRadius, y-smallRadius, x+smallRadius, y+smallRadius, width=5, fill=colors[coloring[id_number][i]])

        # Increment the angle
        angle += angle_increment


# Schedule the callback function to be called after 1000 milliseconds
window.after(200, populate)

# Run the Tkinter event loop
window.mainloop()


