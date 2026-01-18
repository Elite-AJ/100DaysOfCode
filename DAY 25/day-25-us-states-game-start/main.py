import turtle
import pandas

sc = turtle.Screen()
sc.title("U.S States Game")
image = "C:/Users/HP-PC/Desktop/100DOC/Day 25/day-25-us-states-game-start/blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:/Users/HP-PC/Desktop/100DOC/Day 25/day-25-us-states-game-start/50_states.csv")
state_name = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer = sc.textinput(title= f"{len(guessed_states)}/50 States Correct", 
                          prompt= "What's another state's name?").title()

    if answer == "Exit":
        missing_states = [state for state in state_name if state not in guessed_states]
        print(missing_states)
        new_Data = pandas.DataFrame(missing_states)
        new_Data.to_csv("States_to_Learn.csv") 
        break

    if answer in state_name:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)


#sc.exitonclick()






turtle.mainloop()