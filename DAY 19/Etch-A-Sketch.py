from turtle import Turtle, Screen

fred = Turtle()
sc = Screen()

def move_forward():
    fred.fd(10)

def move_backward():
    fred.bk(10)
    
def turn_right():
    fred.rt(10)

def turn_left():
    fred.lt(10) 

def clear():
    fred.clear()
    fred.penup()
    fred.home()
    fred.pd()

sc.listen()
sc.onkey(move_forward, "w")
sc.onkey(move_backward, "s")
sc.onkey(turn_left, "a")
sc.onkey(turn_right, "d")
sc.onkey(clear, "c")
sc.exitonclick()