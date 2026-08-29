from turtle import Turtle, Screen
import pandas

guessed_states = []
t = Turtle()
p = Turtle()

s = Screen()
s.title("U.S. State Game")
image = "blank_states_img.gif"
s.addshape(image)
t.shape(image)
t.goto(0,0)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

game_is_on = True
while game_is_on:
    state_name = s.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="Enter a state")
    state_name_title = state_name.title()

    for state in states:
        index = states.index(state)
        if state_name_title == state:
            if state not in guessed_states:
                guessed_states.append(state)
                p.penup()
                p.hideturtle()
                p.goto(x_cor[index], y_cor[index])
                p.write(f"{state}")
    if len(guessed_states) == 50:
        p.goto(0,0)
        p.write("You Guessed them all!")
        game_is_on = False

    elif state_name_title == "Exit":
        not_guessed_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         not_guessed_states.append(state)
        data = pandas.DataFrame(not_guessed_states)
        data.to_csv("not_guessed_states.csv")
        game_is_on = False