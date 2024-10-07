from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):

        self.snake_body = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):

        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move_snake(self):

        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            position = self.snake_body[seg_num - 1].position()
            self.snake_body[seg_num].goto(position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)







