from turtle import Turtle, Screen
import random

sc = Screen()
sc.setup(width = 500, height = 500)

start_race = False
users_bet = sc.textinput(title= "Make your bet", prompt= "Which turtle would win the race? Enter a colour: ").lower
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -120

all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto (x, y)
    y += 50
    all_turtles.append(new_turtle)

if users_bet:
    start_race = True

while start_race:

    for i in all_turtles:
        if i.xcor() > 230:
            start_race = False
            winning_colour = i.pencolor()
            if winning_colour == users_bet:
                print(f"You've won! The {winning_colour} turtle is the winner")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner")
        rand_distance = random.randint(0, 10)
        i.fd(rand_distance)
sc.exitonclick()