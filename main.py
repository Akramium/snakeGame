from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_tail()

    if snake.head.xcor() > 290 \
            or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 \
            or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for tail in snake.segments[1:]:
        if snake.head.distance(tail) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
