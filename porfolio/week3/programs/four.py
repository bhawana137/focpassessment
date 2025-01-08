''' Modify your program again so that the chosen password cannot be one of a list of
 common passwords, defined thus:
 BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''

# This program helps to set a password

# List of bad passwords that are not allowed
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Ask the user to create a password
pass_1 = input("Create a new password (8-12 characters): ")

# Keep asking until the password is valid
while len(pass_1) < 8 or len(pass_1) > 12 or pass_1 in BAD_PASSWORDS:
    if pass_1 in BAD_PASSWORDS:
        print("Error: That password is too common. Choose something else.")
    else:
        print("Error: Password must be between 8 and 12 characters.")
    pass_1 = input("Please create a new password (8-12 characters): ")

# Ask the user to confirm the password
pass_2 = input("Confirm your password: ")

# Check if both passwords match
if pass_1 == pass_2:
    print("Your password has been successfully set!")
else:
    print("Error: The passwords do not match. Please try again.")
