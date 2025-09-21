from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
ball_direction = (10, 10)
while game_is_on:
  screen.update()
  time.sleep(0.1)

  # Detect ball collision with wall
  if (ball.ycor() >= screen.window_height()/2 - 20):
    ball_direction = (10, -10)
  elif(ball.ycor() <= -(screen.window_height()/2 - 20)):
    ball_direction = (10, 10)

  ball.move(ball_direction[0], ball_direction[1])

screen.mainloop()