def is_leap_year(year):
    # Write your code here. 
    # Define return values for leap year and non-leap year
    leap = "True"
    no_leap = "False"
    
    # Check if year is divisible by 4 but not by 100
    if year % 4 == 0 and year % 100 != 0:
        return(leap)
    
    # Check if year is divisible by 100 but also divisible by 400
    elif year % 100 == 0 and year % 400 == 0:
        return(leap)
    
    # If none of the above, it's not a leap year
    else:
        return(no_leap)
    # Don't change the function name.

# Get user input for the year
year = int(input("Enter the year to be checked: "))

# Call the function and store the result
check_year = is_leap_year(year)

# Output the result
print(check_year)