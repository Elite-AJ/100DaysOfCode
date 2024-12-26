import art  # Importing the 'art' module for the logo display

print(art.logo)

# Define arithmetic functions
#Addition
def add(n1, n2):
    return n1 + n2

#Subtraction
def sub(n1, n2):
    return n1 - n2

#Division
def div(n1, n2):
    return n1 / n2

#Multiplication
def mult(n1, n2):
    return n1 * n2

# Map operators to functions
operation = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

# Get the first number
n1 = int(input("Enter first digit: "))

# Loop for repeated operations
basis = True
while basis == True:
    # Show available operators
    for i in operation:
        print(i)
    
    # Get operator and second number
    my_favourite_op = input("Enter an of the following operators: ")

    n2 = int(input("Enter next digit: "))

    # Perform the operation and Display result
    if my_favourite_op == "+":
        result = add(n1, n2)
        print(f"{n1} {my_favourite_op} {n2} = {result}")
    elif my_favourite_op == "-":
        result = sub(n1, n2)
        print(f"{n1} {my_favourite_op} {n2} = {result}")
    elif my_favourite_op == "/":
        result = div(n1, n2)
        print(f"{n1} {my_favourite_op} {n2} = {result}")
    elif my_favourite_op == "*":
        result = mult(n1, n2)
        print(f"{n1} {my_favourite_op} {n2} = {result}")
    
    # Ask to continue
    ask = input ("Do you want to continue calculating with the previous result? yes/no  ")
    if ask == "yes":
        n1 = result
        basis = True
    else:
        basis = False
        print ("\n" * 100)