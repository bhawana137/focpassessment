''' Write a program that displays the "Seven Times Table". That is, the result of
 multiplying 7 by every number from 0 to 12 inclusive. The output might start:
 0 x 7 = 0
 1 x 7 = 7
 2 x 7 = 14
 and so on'''

# Seven Times Table program

# Start from 0 and go up to 12
number = 0
while number <= 12:
    # Multiply by 7 and print the result
    print(number, "x 7 =", number * 7)
    number += 1  # Move to the next number
