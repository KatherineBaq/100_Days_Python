import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

#Load an image as a shape
image = "blank_states_img.gif"  #Gifs are the ones used for turtle
screen.addshape(image)
turtle.shape(image)
turtle.penup()

#Open CSV file with Pandas
data_states = pd.read_csv("50_states.csv")

print(data_states, len(data_states))


#The x,y coordinates are in the 50_states.csv of each state
data_states_names = data_states.state.to_list()
print(data_states_names)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 States Correct",
                                    prompt="What´s another state name?").title()
    if answer_state == "Exit":
        #Creating a list comprehension for missing_states
        missing_states = [state for state in data_states_names if (state not in guessed_states)]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data_states_names:
        if not answer_state in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data_states[data_states.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)


screen.exitonclick()