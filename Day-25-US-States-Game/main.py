import turtle
import pandas

game_is_on = True
correct_guesses = 0

# Screen Setup
screen = turtle.Screen()
screen.setup(726,492)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get data
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
states = data.state.to_list()
print(states)
x_cord = data.x.to_list()
y_cord = data.y.to_list()
guessed_states = []
remaining_states = []

while game_is_on:
    if correct_guesses == 0:
        answer_state = screen.textinput("Guess the State", "Guess a state name" )
    else:
        answer_state = screen.textinput(f"{correct_guesses}/50 states guessed", "Guess a state name")

    if answer_state == 'exit' or correct_guesses > 50:
        game_is_on = False

    for state,x,y in zip(states,x_cord,y_cord):
        if state == answer_state.title():

            answer = turtle.Turtle()
            answer.hideturtle()
            answer.penup()
            answer.goto(x, y)
            answer.write(state)
            correct_guesses += 1
            guessed_states.append(answer_state.title())

for state in states:
    if state not in guessed_states:
        remaining_states.append(state)

new_data = pandas.DataFrame(remaining_states)
new_data.to_csv("states_to_learn.csv")


screen.exitonclick()