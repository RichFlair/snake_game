from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("turtle")

    def create_snake(self):
        for segment in POSITION:
            self.create_segment(segment)

    def create_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.setpos(position)
        self.segments.append(snake)

    def reset(self):
        for seg in self.segments:
            seg.setpos(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("turtle")

    def move_snake(self):
        for segment in range(len(self.segments)-1, 0, -1):
            x = self.segments[segment-1].xcor()
            y = self.segments[segment-1].ycor()
            self.segments[segment].setpos(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
