'''Modify the "Times Table" again so that the user still enters the number of the table,
 but if this number is negative the table is printed backwards. So entering "-7"
 would produce the Seven Times Table starting at "12 times" down to "0 times".'''

# Times Table program

# Ask the user for the number of the table
num = int(input("Enter the number of the times table you want (0-12 or negative for reverse): "))

# Determine if the table is reversed or not
if num >= 0:  # Normal order
    print(f"{num} Times Table:")
    number = 0
    while number <= 12:
        print(number, "x", num, "=", number * num)
        number += 1
else:  # Reverse order
    print(f"{-num} Times Table (Backwards):")
    number = 12
    while number >= 0:
        print(number, "x", -num, "=", number * -num)
        number -= 1
