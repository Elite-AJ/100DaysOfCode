#DAY 4 
##  --- MAJOR PROJECT --- ##
# * ROCK PAPER SCISSORS

## --- MINOR TASKS --- ##
# * Heads or Tails
# * Bankers Roulette - Who will pay the bills.
# * Treasure Map

import random

## --- MINOR TASKS --- ##

# * Minor 1 - Heads or Tails
choice1 = random.randint(0,1)
if choice1 == 1:
    print ('Heads')
else:
    print ('Tails')

# * Minor 2 - Bankers Roulette - Who will pay the bills.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

bankers =  (len(names))
bankers -= 1
card = random.randint(0, bankers)
bill = names[card]
print (f"{bill} is going to buy the meal today!")

# * Minor 3 - Treasure Map : Allocate the treasure llocation with an "X"
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
n_column = position[0]
n_row = position[1]

column = (int(n_column))
column -= 1
print(column)

row = (int(n_row))
row -= 1
treasure = 'x'
print(row)
map1[row][column] = treasure
print(f"{row1}\n{row2}\n{row3}")


##   ---- MAJOR TASK :- ROCK PAPER SCISSORS ----   ##
rock  = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("Rock Paper Scissors: \n")
print (choice)
if choice == "Rock":
    print(rock)
elif choice == "Paper":
    print(paper)
else:
    print(scissors)
choice_list = [rock, paper, scissors]

ai_choice = random.randint(0,2)

rps = choice_list[ai_choice]
print ("Computer chose:")
print (rps)

#conditional statement for Rock
if choice == "Rock":
    if ai_choice == 2:
        rock = True
        print("You win")
    elif ai_choice == 1:
        rock = False
        print("You lose")
    else:
        print("It's a draw")
#conditional statement for Paper
elif choice == "Paper":
    if ai_choice == 0:
        paper = True
        print("You win")
    elif ai_choice == 2:
        paper = False
        print("You lose")
    else:
        print("It's a draw")
        #conditional statement for Scissors
elif choice == "Scissors":
    if ai_choice == 1:
        scissors = True
        print("You win")
    elif ai_choice == 2:
        rock = False
        print("You lose")
    else:
        print("It's a draw")
else:
    print("Invalid Input")
