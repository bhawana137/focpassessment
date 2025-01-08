'''Write a program that simulates the way in which a user might choose a password.
 The program should prompt for a new password, and then prompt again. If the two
 passwords entered are the same the program should say "Password Set" or
 similar, otherwise it should report an error.'''

#ask the user to create a password
pass_1 = input ("Create a new password:")

#ask the user to confirm the password
pass_2 = input ("Confirm your pasword:")

#check if both passwords match
if pass_1 == pass_2:
    print ("Your password has been successfully set!")
else:
    print("Error: The passwords do not match, Please try again.")