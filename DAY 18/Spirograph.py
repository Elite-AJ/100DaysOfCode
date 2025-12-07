import random
import turtle as t

fred = t.Turtle()
sc = t.Screen()
t.colormode(255)

fred.shape("triangle")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_list = (r, g, b)
    return colour_list

fred.ht()
fred.speed("fastest")

def draw_spirograph(space_inbtween):
    for i in range(int(360 / space_inbtween)):
        fred.color(random_colour())
        fred.circle(100)
        fred.setheading(fred.heading() + space_inbtween)

draw_spirograph(2)

sc.exitonclick()
