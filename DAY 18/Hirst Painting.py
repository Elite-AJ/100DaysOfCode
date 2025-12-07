import random
import turtle as fred
# import colorgram

fred.colormode(255)
sc = fred.Screen()

# rgb_colours = []
# colors = colorgram.extract('hirst_painting.jpg', 43)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.
#     b = color.rgb.b
#     new_colours = (r, g, b)
#     rgb_colours.append(new_colours)

# print(rgb_colours)

colour_list = [
    (249, 228, 19), (234, 251, 243), (213, 13, 9), (196, 13, 36), (196, 69, 21), (230, 228, 6), (235, 148, 39), 
    (33, 90, 188), (43, 212, 72), (33, 30, 151), (16, 23, 54), (66, 9, 49), (243, 40, 149), (14, 206, 223), 
    (68, 202, 228), (64, 21, 11), (223, 21, 110), (16, 154, 21), (227, 167, 10), (248, 11, 9), 
    (98, 75, 9), (244, 58, 17), (222, 140, 201), (71, 240, 160), (11, 97, 63), (6, 39, 33), (73, 216, 156), 
    (238, 157, 208), (86, 79, 205), (92, 224, 233), (249, 9, 13), (242, 166, 158), (178, 180, 226), (32, 243, 172), (5, 83, 117)
 ]

fred.speed("fastest")
fred.ht()
fred.penup()
y = -200
fred.setpos(-250, y)

for i in range(10):
    for i in range (10):
        fred.pd()
        fred.dot(20, random.choice(colour_list))
        fred.penup()
        fred.fd(50)
    y += 50    
    fred.setpos(-250, y)
sc.exitonclick()