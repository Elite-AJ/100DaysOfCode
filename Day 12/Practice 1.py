def is_prime(num):
    if num <= 1:
        return (False)
    if num <= 3:
        return (True)
    if num % 2 == 0 or num % 3 == 0:
        return (False)

# Test the function with the number 5
print (is_prime(5))