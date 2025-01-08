'''Modify your program a final time so that it executes until the user successfully
 chooses a password. That is, if the password chosen fails any of the checks, the
 program should return to asking for the password the first time.'''

# This program helps you set a password

# List of bad passwords that are not allowed
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Loop until a valid password is chosen and confirmed
while True:
    # Ask the user to create a password
    pass_1 = input("Create a new password (8-12 characters): ")

    # Check the password's length and if it's a common password
    if len(pass_1) < 8 or len(pass_1) > 12:
        print("Error: Password must be between 8 and 12 characters.")
        continue
    if pass_1 in BAD_PASSWORDS:
        print("Error: That password is too common. Choose something else.")
        continue

    # Ask the user to confirm the password
    pass_2 = input("Confirm your password: ")

    # Check if both passwords match
    if pass_1 == pass_2:
        print("Your password has been successfully set!")
        break
    else:
        print("Error: The passwords do not match. Please try again.")
