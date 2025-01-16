''' Another way to hide a message is to include the letters that make it up within
 seemingly random text. The letters of the message might be every fi h character,
 for example. Write and test a function that does such encryption. It should
 randomly generate an interval (between 2 and 20), space the message out
 accordingly, and should fill the gaps with random letters. The function should
 return the encrypted message and the interval used.
 For example, if the message is "send cheese", the random interval is 2, and for
 clarity the random letters are not random:
 send cheese
 s  e  n  d   c  h  e  e  s  e
 sxyexynxydxy cxyhxyexyexysxye '''

import random
import string

def encrypt_message(msg):
    # Generate a random interval between 2 and 20
    step = random.randint(2, 20)
    
    # Remove spaces from the message
    msg = msg.replace(" ", "")
    
    # Start with an empty encrypted message
    encrypted = ""
    
    for letter in msg:
        # Add the actual letter to the encrypted message
        encrypted += letter
        # Add (step - 1) random letters after it
        for _ in range(step - 1):
            encrypted += random.choice(string.ascii_lowercase)
    
    return encrypted, step

# Ask the user for input
user_message = input("Enter a message to encrypt: ")
result, interval = encrypt_message(user_message)

# Show the results
print(f"Encrypted message: {result}")
print(f"Interval used: {interval}")
