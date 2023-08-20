#DAY 2 Goals

#** Data Types, Numbers, Type conversions and f-strings

##**Create a tip calculator 
#*/Identify the total bill
# Identify how many ways the bill is to be split
#Input the percentage for the tip charge

#Tip Generator

print("Welcome to the Tip calculator!")
bill = (float(input("What was the total bill? \n$")))
tip = (int(input("How much tip would you like to give? 10, 12, or 20? \n")))
people = (int(input('How many people are to split the bill? \n')))

#The maths behind the code.
tipPercen = tip / 100
total_tip = bill * tipPercen
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
