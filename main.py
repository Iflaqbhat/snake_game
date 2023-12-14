from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

X = 190
W = -190
Y = 190
Z = -190
screen = Screen()
screen.tracer(0)
screen.setup(width=400, height=400)
screen.bgcolor("black")
screen.title("My Snake Game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #     detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #   detect collision with wall
    if snake.head.xcor() > X or snake.head.xcor() < W or snake.head.ycor() > Y or snake.head.ycor() < Z:
        game_is_on = False
        scoreboard.game_over()

    for segement in snake.segements:
        if segement == snake.head:
            pass
        elif snake.head.distance(segement) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
