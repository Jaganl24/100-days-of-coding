from turtle import Screen, Turtle
import random
# setup
all_turtles = []
is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ['red', 'orange','yellow', 'green','blue', 'purple']
y_coordinates = [-70, -40, -10, 20, 50, 80]

# creation of turtle objects
for i in range(0,6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y= y_coordinates[i])
    all_turtles.append(turtle)
# sets while loop to start race
if choice:
    is_race_on = True
# while for race
while is_race_on:
# moves each turtle by random amount
    random_distance = random.randint(0,10)
    current_turtle = random.choice(all_turtles)
    current_turtle.forward(random_distance)

# Checks for winner
    for i in range(0,6):
        if all_turtles[i].xcor() > 200:
            if all_turtles[i].color() == choice:
                print(f"Congrats, your turtle won")
            else:
                print(f"You lose. The {all_turtles[i].color()[0]} turtle is the winner")
            is_race_on = False


screen.exitonclick()
