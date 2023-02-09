from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.title("Breakout Game")
screen.bgcolor('black')
screen.setup(800, 600)
screen.cv.config(cursor='none')
screen.tracer(0)
block_list = []
score = 0
lives = 5

paddle = Paddle(screen)
ball = Ball(paddle)
scoreboard = Scoreboard()

c_l = ['#FF7077', '#FFB067', '#2FF3E0', '#F8D210', '#FA26A0', '#F51720', '#4C5270', '#C3B330', '#22AAC0', '#146C80']

for j in range(120, 240, 25):
    for i in range(-360, 370, 65):
        block = Block()
        block.color(random.choice(c_l))
        block.goto(i, j)
        block_list.append(block)


while len(block_list) > 0 and lives > 0:

    screen.update()
    time.sleep(0.017)
    ball.move()

    # Border bounce
    if ball.xcor() <= -380 or ball.xcor() >= 380:
        ball.bounce_x()
    if ball.ycor() >= 280:
        ball.bounce_y()
    if ball.ycor() < -300:
        ball.reset()
        lives -= 1
        scoreboard.clear()
        scoreboard.write(f'Score: {score}  Lives: {lives}', align='center', font=('Courier', 24, 'normal'))

    # Paddle bounce
    # if (-240 <= ball.ycor() <= -230) and (
    #         paddle.xcor() - 100 < ball.xcor() < paddle.xcor() + 100) and ball.dy < 0:
    #     ball.bounce_y()

    if (paddle.xcor() - 100 < ball.xcor() < paddle.xcor() + 100) and (-240 <= ball.ycor() <= -230) and ball.dy < 0:
        if paddle.xcor() > 0:
            if ball.xcor() > paddle.xcor():
                ball.bounce_x()
                ball.bounce_y()
            else:
                ball.bounce_y()
        elif paddle.xcor() < 0:
            if ball.xcor() < paddle.xcor():
                ball.bounce_x()
                ball.bounce_y()
            else:
                ball.bounce_y()
        else:
            if ball.xcor() > paddle.xcor() or ball.xcor() < paddle.xcor():
                ball.bounce_x()
                ball.bounce_y()
            else:
                ball.bounce_y()

    # Block collision check
    for i in block_list:
        if (i.ycor() - 20 <= ball.ycor() <= i.ycor() + 20) and (
                i.xcor() - 60 < ball.xcor() < i.xcor() + 60):
            i.goto(1000, 1000)
            ball.bounce_y()
            block_list.remove(i)
            score += 1
            scoreboard.clear()
            scoreboard.write(f'Score: {score}  Lives: {lives}', align='center', font=('Courier', 24, 'normal'))

screen.clear()
screen.bgcolor('black')
scoreboard.clear()
scoreboard.goto(0, -20)
if lives == 0:
    result = "You Lose"
else:
    result = "You Won!!!"
scoreboard.write(f'{result}\nScore: {score}\nLives: {lives}', align='center', font=('Courier', 40, 'normal'))
screen.mainloop()
