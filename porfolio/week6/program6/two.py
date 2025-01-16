'''  Write and test a function that takes an integer as its parameter and returns the
 factors of that integer. (A factor is an integer which can be multiplied by another to
 yield the original) '''

def find_factors(n):
    # First, check if the number is positive
    if n <= 0:
        return "Enter a positive integer"
    
    # Initialize an empty list to store the factors
    factors = []
    
    # Loop through all numbers from 1 to n
    for i in range(1, n+1):
        if n % i == 0:  # If i divides n with no remainder, it's a factor
            factors.append(i)
    
    return factors

# Testing the function
number = 15
result = find_factors(number)
print(f"The factors of {number} are {result}")
