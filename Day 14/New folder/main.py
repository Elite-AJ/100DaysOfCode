#Display Art
from art import logo, versus
print (logo)
import random
from gamedata import data as data

#Format the account data into a printable format
score = 0
continue_game = True

while continue_game == True:
    def format_data(account):
        account_name = account["name"]
        account_desc = account["job"]
        account_country = account["country"]
        return f"{account_name}, a {account_desc} from {account_country}."


    def check(guess, a_follow_count, b_follow_count):
        if a_follow_count > b_follow_count: 
            return guess == "a"
        else:
            return guess == "b"

    #Generate a random account from the game data
    if score == 0:
        account_a = random.choice(data)
        account_b = random.choice(data)
    else:
        account_a = account_b
        account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print (f"Compare A: {format_data(account_a)}")
    print (versus)
    print (f"Against B: {format_data(account_b)}")

    #User Guess 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()



    #Clear screen
    print ("\n" * 20)
    

    print (logo)

    #Check if user is correct
    ## Get follower count
    a_follow_count = account_a["followers"]
    b_follow_count = account_b["followers"]

    ##Use if statement to check correctness
    is_correct = check(guess, a_follow_count, b_follow_count)

    #Give feedback on their guess 
    if is_correct:
        score += 1
        print (f"You guessed right! Current Score = {score}")
    else:
        print(f"Sorry, you are wrong. Final Score = {score}")
        continue_game = False