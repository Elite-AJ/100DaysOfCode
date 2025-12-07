from turtle import Turtle, Screen
import random

fred = Turtle()
sc = Screen()

fred.shape("triangle")

# for i in range(4):
    # fred.forward(100)
    # fred.right(90)

fred.penup()
fred.goto(-100,100)
fred.pendown()

colour_list = [
    "aliceblue", "aquamarine", "bisque", "blanchedalmond", "burlywood",
    "cadetblue", "chartreuse", "coral", "cornflowerblue", "crimson",
    "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen",
    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid",
    "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray",
    "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray",
    "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia"
]

def draw_polygons(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        fred.fd(100)
        fred.right(angle)
        

for shapes in range (3,11):
        fred.color(random.choice(colour_list))
        draw_polygons(shapes)



# for i in range(25):
#     fred.forward(10)
#     fred.penup()
#     fred.forward(10)
#     fred.pendown()

# for i in range(3):
#     fred.fd(100)
#     fred.right(120)

# fred.color("red")
# for i in range(4):
#     fred.fd(100)
#     fred.right(90)

# fred.color("yellow")
# for i in range(5):
#     fred.fd(100)
#     fred.right(72)

# fred.color("brown")
# for i in range(6):
#     fred.fd(100)
#     fred.right(60)

# fred.color("pink")
# for i in range(7):
#     fred.fd(100)
#     fred.right(51.43)

# fred.goto(-100,0)
# fred.color("blue")
# for i in range(8):
#     fred.fd(100)
#     fred.right(45)

# fred.color("orange")
# for i in range(9):
#     fred.fd(100)
#     fred.right(40)

# fred.color("purple")
# for i in range(10):
#     fred.fd(100)
#     fred.right(36)


sc.exitonclick() 