from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# initialize snake,food and scoreboard as well as game over functionality

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# set movement commands using keyboard
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

# detect collision with food and update food location and scoreboard
    if snake.head.distance(food) < 15:
        food.new_location()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.extend()

# wall detection
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False

# tail detection
    for segment in snake.snake_body[2:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()
