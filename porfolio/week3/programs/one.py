'''Modify your greeting program so that if the user does not enter a name (i.e. they
 just press enter), the program responds "Hello, Stranger!". Otherwise it should print
 a greeting with their name as before'''

# asking the user for their name
name = input ("Enter your name:")

# check if the user entered a name or just pressed Enter
if name == "":
    print("Hello,Stranger!")
else:
    print(f"Hello, {name}!")