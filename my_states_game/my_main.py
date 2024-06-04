import turtle
import pandas
from state_name_writer import State_writer


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

state_writer = State_writer()
data = pandas.read_csv("50_states.csv")
state_list = data.state

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    for state in state_list:
        if answer_state == state:
            state_data = data[data.state == state]
            state_writer.goto(int(state_data.x),int(state_data.y))
            state_writer.write(state)







screen.exitonclick()