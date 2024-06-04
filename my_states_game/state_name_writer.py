from turtle import Turtle

FONT = "Courier",14,"normal"

class State_writer(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()


    def create_turtle(self):
        self.hideturtle()
        self.penup()

    def write_state(self,state):
        self.write(state,align="center",font=FONT)

    def turtle_go(self,x,y):
        self.goto(x,y)