#-----------MAJOR TASK-----------

#----------THE SECRET auction PROGRAM----------

#insert the appropriate ASCII art
import Art

from Art import gavel
print (gavel)

#Create Dict
auction = {}

#create while loop to aid bidding 
bidding = True

while bidding == True:

    #collect data
    #Ask for name input
    name = input("What is your name? ")

    #Ask for name input
    bid = int(input("What's your bid? $"))

    #Add name and Bid into the disctionary
    auction[name] = bid

    #Run conditional statement to ask if there are still more users
    bidding = input("Are there any other user ready to bid? Yes/No  ")
    if bidding == "Yes":
        print("\n" * 100)
        bidding = True
    elif bidding == "yes":
        print("\n" * 100)
        bidding = True
    elif bidding == "YES":
        print("\n" * 100) 
        bidding = True
    else:
        bidding = False

#Finding the winner
x = 0
winner = ""
for key, values in auction.items():
    if values > x:
        x = values
        winner = key
print (auction)
print (f"Congratulations, the winner is {winner} with the highest bid of ${x}.")
