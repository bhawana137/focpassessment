'''Write and test a function that determines if a given integer is a prime number. A
 prime number is an integer greater than 1 that cannot be produced by multiplying
 two other integers.  '''

def is_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        return False  
    
    # Check for divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:  # If n is divisible by i, it's not a prime number
            return False
    
    # If no divisors were found, n is a prime number
    return True

# Taking user input
num = input("Enter a number: ")

# Try to convert the input to an integer
try:
    number = int(num)  # Convert input to an integer

    # Check if the number is prime
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
