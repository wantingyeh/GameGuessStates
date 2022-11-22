import turtle
from pen import Pen
import pandas as pd

# set up: screen with the image
screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"
## add image
screen.addshape(img)
turtle.shape(img)


# print(answer_state)

pen = Pen()

# get the x, y coordinate from the screen turtle
# def get_mouse_clck_coor(x,y):
#     print(x,y)
#
# # listen when the mouse clicks of the x, y coordinate
# turtle.onscreenclick(get_mouse_clck_coor)
# turtle.mainloop()

# load the dataset from the csv
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
data_country = data["state"]
#print(data_country)


score = 0
guess_state = []

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title= f"{score}/50 State Correct",
                                    prompt="What's another state's name?").title()
    if score == 50:
        game_is_on = False

    elif answer_state == "Exit":
        break

    # if the answer_state is one of the states then we need the turtle to go to the position to write the name
    elif answer_state in all_states:
        state_data_row = data[data.state == answer_state]
        pen.write_text(int(state_data_row.x), int(state_data_row.y), answer_state)
        score += 1
        guess_state.append(answer_state)

        # pen.write_text(x_axis, y_axis, answer_state)


# generate a "state_to_learn.csv"
## should contain the states that NOT being guessed by the users

missing_state_dic = {
    "Missing states": list(set(all_states) - set(guess_state))}

missing_state = pd.DataFrame(missing_state_dic)
missing_state.to_csv("state_to_learn.csv")