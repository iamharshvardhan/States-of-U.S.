import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States", prompt="Answer:").title()
    if answer == "Exit":
        missing_states_list = [missing_states for missing_states in states if missing_states not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_remember.csv")
        break
    if answer in states:
        guessed_state.append(answer)
        ans = turtle.Turtle()
        ans.penup()
        ans.hideturtle()
        state_data = data[data.state == answer]
        ans.goto(int(state_data.x), int(state_data.y))
        ans.write(answer)

screen.exitonclick()
