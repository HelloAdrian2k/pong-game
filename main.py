from turtle import Turtle, Screen

def go_up():
  new_ycor = paddle.ycor() + 20
  paddle.goto(paddle.xcor(), new_ycor)

def go_down():
  new_ycor = paddle.ycor() - 20
  paddle.goto(paddle.xcor(), new_ycor)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_is_on = True
while game_is_on:
  screen.update()

screen.mainloop()