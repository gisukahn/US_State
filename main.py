import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")
t = turtle.Turtle()
t.penup()
t.hideturtle()
guessed_state = []
all_state = data.state.to_list()
append_to_Csv = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State", prompt="What's another state's name?")
    if answer_state in all_state:
        x_cor = (data[data.state == answer_state].iat[0,1])
        y_cor = (data[data.state == answer_state].iat[0,2])
        state_Name = (data[data.state == answer_state].iat[0, 0])
        t.setposition(x_cor, y_cor)
        guessed_state.append(state_Name)
        t.write(state_Name)
    if answer_state=="exit":
        for item in all_state:
            if item in guessed_state:
                pass
            else:
                append_to_Csv.append(item)
        new_data = pandas.DataFrame(append_to_Csv)
        new_data.to_csv("Missing_States")
        break;




turtle.mainloop()


