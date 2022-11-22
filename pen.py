from turtle import Turtle

ALIGHN = "center"
FONT = ('Arial', 8, 'normal')

class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_text(self, x, y, answer):
        self.goto(x, y)
        self.write(answer, align=ALIGHN, font=FONT)
