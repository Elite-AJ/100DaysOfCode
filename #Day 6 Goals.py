#Day 6#
#CodeBlocks, Indentation, While Loop
def turn_upward:
	turn_left()
	move()
while at_goal() == False:
	if wall_in_front() == True:
		turn_left()
	while move():
		if wall_in_front() == True:
			move()
		else:
			jump()
	else:
		move
	print(at_goal())

#Hurdle_4
def turn_right():
turn_left()
turn_left()
turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()

while at_goal() == False:
    if wall_in_front():
        jump()
    else:
        move()

#Maze
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and not wall_in_front():
        move()
    else:
        turn_left()