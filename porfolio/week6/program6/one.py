'''  Write a function that accepts a positive integer as a parameter and then returns a
 representation of that number in binary (base 2) '''

def to_binary(n):
    # First, we check if the number is positive
    if n <= 0:
        return "Input must be a positive integer"
    
    # Initialize an empty string to build the binary representation
    binary_str = ""
    
    while n > 0:
        remainder = n % 2   #
        binary_str = str(remainder) + binary_str  # Add remainder to the front of the string
        n = n // 2  # Divide n by 2 (integer division)
    
    # After the loop finishes, return the binary string
    return binary_str

# Testing the function
number = 20  
binary_rep = to_binary(number)
print("The binary representation of", number, "is", binary_rep)
