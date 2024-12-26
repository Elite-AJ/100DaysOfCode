def is_prime(num):
    # Return False if number is less than or equal to 1
    if num <= 1:
        return False
    
    # Return True if number is 2 or 3
    elif num <= 3:
        return True
    
    # Return False if number is divisible by 2 or 3
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    # Start checking for factors from 5
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6  # Check next possible factors (i and i+2)

    # If no factors found, the number is prime
    return True