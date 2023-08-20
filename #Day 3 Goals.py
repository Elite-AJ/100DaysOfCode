#Treasure Hunt Game Development --- MAJOR TASK

### ---MINOR TASKS--- ###

# Odd or Even
## Can tell if the given input(number) is either an even or an dd number
number = int(input("Which number do you want to check? "))
#applying conditional statement
if number % 2 == 0:
	print('This is an even number.')
else:
	print('This is an odd number')




#BMI 2.0
## It interpretes the Body Mass Index based on user's weight and height

print("Welcome to the BMI 2.0 Calculator")

# Collecting the needed variables
height = float(input("Please enter your height in m\n"))
weight = float(input("Please enter your weight in kg\n"))

# Entering the Calculations
bmi = weight / (height ** 2)

#Entering conditions for the BMI values
# ---Clinically Obese---
if bmi > 35:
	print(f"Your BMI is {bmi}, you are clinically obese")
# ---Obese---
elif bmi > 30 and bmi < 35:
	print(f"Your BMI is {bmi}, you are obesed")
# ---Slightly Overweight---
elif bmi > 25 and bmi < 30:
	print(f"Your BMI is {bmi}, you are slightly overweight")
# ---Normal Weight---
elif bmi > 18.5 and bmi < 25:
	print(f"Your BMI is {bmi}, you have a normal weight")
# ---Clinically Obese---
else:
	print(f"Your BMI is {bmi}, you are underweight")





# Leap Year
#Conditions
# 1. If the year is evenly divisible by 4 - Leap year
# 2. If the year is evenly divisible by 100 - Not a leap year
# 3. If the year is evenly divisible by 400 - Leap year

year = int(input("Enter the year to be checked: "))
x = int(input('Choose any year:  '))
leap = "Leap Year"
no_leap = "No Leap Year"

if x % 4 == 0 and x % 100 != 0:
    print(leap)
elif x % 100 == 0 and x % 400 == 0:
    print(leap)
else:
    print(no_leap)
            




#     ---Pizza Order Programme---
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
	size = "S"
	bill = 15
elif size == "M":
	size = "M"
	bill = 20
elif size == "L":
	size = "L"
	bill = 25

if add_pepperoni == "Y":
	if size == "S":
		bill += 2
	elif size == "M" or "L":
		bill += 3
	else:
		bill += 0

if extra_cheese == "Y":
	bill += 1
else:
	bill += 0
print(f"Your final bill is: ${bill}")





#           ---LOVE CALCULATOR---
print("Welcome to the best Love Calculator!\nDo you want to find out how much compatible you are? If yes, Lets go!!!")
name1 = input("What is your name? \n")
name2 = input("What is your partner's name? \n")

combined_name = name1 + name2
lower_case_name = combined_name.lower()

#True check on both names
t = (lower_case_name.count("t"))
r = (lower_case_name.count("r"))
u = (lower_case_name.count("u"))
e = (lower_case_name.count("e"))
true = t + r + u + e
true_x = str(true)

#Love check on both names 
l = (lower_case_name.count("l"))
o = (lower_case_name.count("o"))
v = (lower_case_name.count("v"))
e1 = (lower_case_name.count("e"))
love_x = l + o + v + e1

love = str(love_x)

trueLove = true + love
true_love = int(trueLove)

#Conditional Statements
if true_love < 10 or true_love > 90:
	print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
	print(f"Your score is {true_love}, you are alright together.")
else:
	print(f"Your score is {true_love}")






## ----THE MAJOR TASK ---- ##
## ---TREASURE ISLAND ---##
print('''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗                                
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗                               
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║                               
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║                               
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝                               
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝                                
                                                                                                                   
████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗    ██╗███████╗██╗      █████╗ ███╗   ██╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝    ██║██╔════╝██║     ██╔══██╗████╗  ██║██╔══██╗
   ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗      ██║███████╗██║     ███████║██╔██╗ ██║██║  ██║
   ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝      ██║╚════██║██║     ██╔══██║██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗    ██║███████║███████╗██║  ██║██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 

''')
treasure_name = input("What is your name?\n")
print(f'Welcome to treasure Island {treasure_name}, Your mission is to find the treasure.')
entry = input('''Welcome once again to the funniest treasure hunt challange on the web, hahaha!!!
Please enter your answers in the format its presented in. Thank you

Are you ready to find the missing treasure?				
		(ง'̀-'́)ง
YES / NO

''')
if entry  == "YES":    
        print(f'''Quest for the Lost Key: Treasure Island Adventure
	In the heart of a bustling coastal town, rumors of a long-lost treasure on a mysterious island have captured the imagination of treasure hunters,
	adventurers, and thrill-seekers alike.
	
	The island, aptly named Treasure Island, holds secrets that have eluded discovery for generations.
	
	The legend tells of an ancient key that can unlock the location of the hidden riches.

	Pah-pa-ra!!! The gong sounded and all the adventurers and treasure hunters gathered as a the man began to speak.

	{treasure_name}: Who's that geezer?
	Random Hunter: That's the Mayor of Trintana.

	The mayor, an enthusiastic historian, recounts the tale of Captain Morgan's fabled treasure said to be buried on the island.
	
	However, the treasure's exact whereabouts remain unknown, guarded by riddles, clues, and obstacles crafted by the captain himself.
	
	Mayor: "You'd be handed a map but the directions and choice would be made by you. With that been said, may the hunt begin!!!"



                  ___________________________________________________________________
                 / \-----     ---------  -----------     -------------- ------    ---\\
                 \_/_________________________________________________________________/
                 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
                 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
                 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
                 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
                 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
                 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
                 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
                 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
                 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
                 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
                 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
                 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
                 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
                 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
                 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
                 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
                 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
                 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
                 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
                 |____~____~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
                 / \----- ----- ------------  ------- ----- -------  --------  ------\\
                 \_/_________________________________________________________________/



		''')
        ready_charge = input("The hunt begins and you get to a cross path with left and right directions.\nWhich do you pick?\nL or R\n")
        if ready_charge == "L":
                print('You move to the left and you approach a very large river.')
                swim_wait = input('Do you wait or swim over the river?\nswim/wait:   ')
                if swim_wait == "wait":
                        print('A rickety ship arrives. You get into the ship. As you move around the ship, you enter a door and a voice announces,\n"Before you are three doors colours RED, YELLOW and BLUE.\nIn one of these doors is the key to the treasure and\non the left extreme corner of that room the treasure."')
                        select_door = input(f"Which door do you go into {treasure_name}? R, Y or B:\n")
                        if select_door == "Y":
                                print(f'''Congratulations {treasure_name}, You've found the key and you opened your treasure


				*******************************************************************************
				          |                   |                  |                     |
				 _________|________________.=""_;=.______________|_____________________|_______
				|                   |  ,-"_,=""     `"=.|                  |
				|___________________|__"=._o`"-._        `"=.______________|___________________
				          |                `"=._o`"=._      _`"=._                     |
				 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
				|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
				|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
				          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
				 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
				|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
				|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
				____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
				/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
				____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
				/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
				____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
				/______/______/______/______/______/______/______/______/______/______/_______/
				*******************************************************************************		        

				                               	      THE END
				''')
                        elif select_door == "R":
                                print('Burned by fire.\nGAME OVER!!!')
                        elif select_door == "BLUE":
                                print("You got eaten by beasts.\nGAME OVER!!!")
                        else:
                                print('GAME OVER!!!')
                else:
                        print("You are attacked by a trout and your remains is fed to the vultures.\nGAME OVER!!!")
        else:
                print(f"Too bad for you {treasure_name}. You fell into a hole\nGAME OVER!!!")
else:
	print(f"Better for you, we eat chickens like {treasure_name} in Treasue Island")
