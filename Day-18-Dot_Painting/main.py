from turtle import Turtle, Screen, colormode
import random
# initializing colours and colour choice, as well as Turtle, Screen and colormode from turtle class
colours_list = [(217, 57, 50), (102, 180, 219), (245, 240, 232), (192, 160, 108), (154, 80, 60), (59, 111, 170), (185, 222, 236), (29, 20, 16), (22, 17, 19), (228, 241, 233)]
colour = colormode(255)
turtle = Turtle()
screen = Screen()
#initalize positon
x = -225
y = -225
# first for loop increments the rows by adding 50 to the y coordinate
# second for loop creates the dots using .dot() and uses tuples in colours_list to select a random color each time
for row in range(1,11):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    y += 50
    for dot in range(1,11):
        turtle.pencolor(random.choice(colours_list))
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

# exit on click of screen
screen.exitonclick()