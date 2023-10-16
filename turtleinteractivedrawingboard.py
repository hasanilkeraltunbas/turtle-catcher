import turtle
import random
import time

# Window settings
turtle.setup(width=750, height=750)
background = turtle.Screen()
background.bgcolor("black")

# Create a turtle
turtie = turtle.Turtle()
turtie.shape("turtle")
turtie.shapesize(2)  # Set the size to 1x1 for the hitbox
turtie.color("yellow")

# Set the speed of the turtle
turtie.speed(1)

# Function for random positioning of the turtle
def change_random_location():
    x = random.randint(-365, 365)  # Random x coordinate
    y = random.randint(-365, 365)
    turtie.penup()  # Do not draw anything
    turtie.goto(x, y)
    time.sleep(0.5)  # Pause for half a second

# Mouse click inputs
def increment_counter(x, y):
    global step_counter, hit_counter
    step_counter += 1
    counter.clear()
    counter.write("Step Count: " + str(step_counter) + " - Hit Count: " + str(hit_counter), align="center", font=("Arial", 16, "normal"))
    # Control for catching the turtle
    x_turtle, y_turtle = turtie.pos()
    if abs(x - x_turtle) < 20 and abs(y - y_turtle) < 20:
        hit_counter += 1

# Add the counter and hit counter
counter = turtle.Turtle()
counter.penup()
counter.color("white")
counter.hideturtle()
counter.goto(0, 350)
counter.write("Step Count: 0 - Hit Count: 0", align="center", font=("Arial", 16, "normal"))

# Start the step counter and hit counter
step_counter = 0
hit_counter = 0

# Listen for mouse click events
turtle.onscreenclick(increment_counter)

# Start an infinite loop
while True:
    change_random_location()
    turtle.update()
