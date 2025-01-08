''' Modify your "Times Table" program so that the user enters the number of the table
 they require. This number should be between 0 and 12 inclusive.'''

# Times Table program

# Ask the user for the number of the table
num = int(input("Enter the number of the times table you want (0-12): "))

# Make sure the number is valid
while num < 0 or num > 12:
    print("Error: Enter a number between 0 and 12.")
    num = int(input("Enter the number of the times table you want (0-12): "))

# Display the chosen times table
print(f"{num} Times Table:")
number = 0
while number <= 12:
    print(number, "x", num, "=", number * num)
    number += 1
