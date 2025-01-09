'''Modify your "greetings" program so that the first letter of the name entered is
 always in uppercase with the rest in lowercase. This should happen even if the user
 entered their name differently. So if the user entered arthur, ARTHUR, or even
 arTHurthe name should be displayed asArthur. '''

# Greetings program

# Ask for the user's name
name = input("Enter your name: ")

# Make the first letter uppercase and the rest lowercase
name = name.capitalize()

# Print the greeting
print("Hello, " + name + "!")

