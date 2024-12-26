import random   # Importing random module
import art  # Importing the 'art' module for the logo display

print(art.logo)

reps = True     # Variable to control the game loop
def game():
    global reps, difficulty_case, repeat  # Accessing global variables

    # Easy difficulty game logic
    if difficulty_case == "easy":
        while repeat:
            num = random.randint(1, 101)    # Random number to guess
            score_attempt = 0
            attempt = 10        # Starting attempts for easy mode
            guess = int(input(f"You have {attempt} attempts, guess the number --  "))
            guess_type = True

            while guess_type == True:
                if attempt > 1:
                    if type(guess) == int:
                        guess_type = True
                        if guess > num:
                            attempt -= 1
                            score_attempt += 1
                            print ("Too high")
                            guess = int(input(f"You have {attempt} attempts, guess the number "))
                            guess_type = True
                        elif guess < num:
                            attempt -= 1
                            score_attempt += 1
                            print ("Too low")
                            guess = int(input(f"You have {attempt} attempts, guess the number "))
                            guess_type = True
                        else:
                            guess = num
                            score = (100 * (1/score_attempt))       # Calculate score
                            print(f"Your guess is correct, SCORE = {score:.2f}%")
                            guess_type = False
                            repeat = False
                            reps = False
                else:
                    guess_type = False
                    reps = False
                    repeat = False
                    print("You've run out of guesses, you lose")
    
    # Hard difficulty game logic
    elif difficulty_case == "hard":
        while repeat:
            num = random.randint(1, 101)
            score_attempt = 0
            attempt = 5     # Starting attempts for hard mode
            guess = int(input(f"You have {attempt} attempts, guess the number --  "))
            guess_type = True

            while guess_type == True:
                if attempt > 1:
                    if type(guess) == int:
                        guess_type = True
                        if guess > num:
                            attempt -= 1
                            score_attempt += 1
                            print ("Too high")
                            guess = int(input(f"You have {attempt} attempts, guess the number "))
                            guess_type = True
                        elif guess < num:
                            attempt -= 1
                            score_attempt += 1
                            print ("Too low")
                            guess = int(input(f"You have {attempt} attempts, guess the number "))
                            guess_type = True
                        else:
                            guess = num
                            score = (100 * (1/score_attempt))
                            print(f"Your guess is correct, SCORE = {score:.2f}%")
                            guess_type = False
                            repeat = False
                            reps = False
                else:
                    guess_type = False
                    reps = False
                    repeat = False
                    print("You've run out of guesses, you lose")

# Initial game start
print('''           Welcome to the Number Guessing Game!
      I'm thinking of a number between 1 and 100.
      ''')

x = input('Do you want to play the game? Y/N  ')
x_case = x.lower()

if x_case == "y":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    difficulty_case = difficulty.lower()
    repeat = True
    game()
else:
    print("Run code again to start")

# Asking if the user wants to play again after the game ends
while reps == False:
    repeat_option = input("Do you want to play again? Y/N  ")
    repeat_option_case = repeat_option.lower()
    if repeat_option_case == "y":
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        difficulty_case = difficulty.lower()
        reps = True
        game()
    elif repeat_option_case == "n":
        print ("Game Over")
        reps = True
    else:
        print("Invalid Entry")
        reps = False