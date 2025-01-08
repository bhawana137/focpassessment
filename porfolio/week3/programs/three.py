''' Modify your previous program so that the password must be between 8 and 12
 characters (inclusive) long.'''

# This program helps you set a password

# Ask the user to create a password
pass_1 = input("Create a new password (8-12 characters): ")

# Keep asking until the password is between 8 and 12 characters long
while len(pass_1) < 8 or len(pass_1) > 12:
    print("Error: Password must be between 8 and 12 characters.")
    pass_1 = input("Create a new password (8-12 characters): ")

# Ask the user to confirm the password
pass_2 = input(" Confirm your password: ")

# Check if both passwords match
if pass_1 == pass_2:
    print("Your password has been successfully set!")
else:
    print("Error: The passwords do not match. Please try again.")
