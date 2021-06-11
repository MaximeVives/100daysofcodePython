from turtle import Turtle, Screen
import pandas


sc = Screen()
sc.title("US States Game")

image = "Ressources/blank_states_img.gif"
sc.addshape(image)


turtle = Turtle(shape=image)

data = pandas.read_csv("Ressources/50_states.csv")

list_states = data.state.to_list()

answer_list_temp = pandas.read_csv("Ressources/answer.csv")
answer_list = []

for ans in answer_list_temp["state"]:
    answer_list.append(ans)

    ctry = Turtle()
    ctry.hideturtle()
    ctry.penup()
    state_data = data[data.state == ans]
    ctry.goto(x=float(state_data.x), y=float(state_data.y))
    ctry.write(arg=ans, align="center")


score = len(answer_list)

while score < len(list_states):
    answer_state = sc.textinput(title=f"{score} sur {len(list_states)}. Name a state", prompt="Enter the name of a US state")

    if answer_state == "Exit":
        print(answer_list)
        answer_export = pandas.Series(answer_list, name="state")
        answer_export.to_csv("Ressources/answer.csv")
        break

    if answer_state in list_states and answer_state not in answer_list:
        score += 1

        ctry = Turtle()
        ctry.hideturtle()
        ctry.penup()
        state_data = data[data.state == answer_state]
        ctry.goto(x=float(state_data.x), y=float(state_data.y))
        ctry.write(arg=answer_state, align="center")

        answer_list.append(answer_state)

if score == 50:
    answer_list = []
    answer_export = pandas.Series(answer_list, name="state")
    answer_export.to_csv("Ressources/answer.csv")

sc.exitonclick()