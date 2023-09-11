from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_score()
        snake.create_segment((snake.segments[-1].xcor(), snake.segments[-1].ycor()))

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
