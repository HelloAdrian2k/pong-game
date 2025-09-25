from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('white')
    self.penup()

  def move(self, x_offset, y_offset):
    new_xcor = self.xcor() + x_offset
    new_ycor = self.ycor() + y_offset
    self.goto(new_xcor,new_ycor)

  def reset_position(self):
    self.goto(0, 0)