from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 160))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
ball_direction = (10, 10)
while game_is_on:
  screen.update()
  time.sleep(0.05)

  # Detect ball collision with wall 
  height_limit = screen.window_height()/2 - 20
  width_limit = screen.window_width()/2 - 20
  x_continue = ball_direction[0]

  if(ball.ycor() >= height_limit):
    ball_direction = (x_continue, -10)
  elif(ball.ycor() <= -height_limit):
    ball_direction = (x_continue, 10)
    
  # Detect paddle collision
  elif(ball.xcor() == width_limit - 40 or ball.xcor() == -(width_limit - 40)):
    y_continue = ball_direction[1]
    if(ball.ycor() <= r_paddle.ycor() + 50 and ball.ycor() >= r_paddle.ycor() - 50):
      ball_direction = (-10, y_continue)
    elif(ball.ycor() <= l_paddle.ycor() + 50 and ball.ycor() >= l_paddle.ycor() - 50):
      ball_direction = (10, y_continue)
  
  # Detect score point to left side
  if(ball.xcor() >= width_limit):
    scoreboard.l_point()
    ball.reset_position()

  # Detect score point to right side 
  if(ball.xcor() <= -width_limit):
    scoreboard.r_point()
    ball.reset_position()

  ball.move(ball_direction[0], ball_direction[1])

screen.mainloop()