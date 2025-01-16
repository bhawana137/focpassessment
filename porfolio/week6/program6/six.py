''' Write a program that decrypts messages encoded as above.'''
import random
import string

# Encryption function (as provided)
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

# Decryption function
def decrypt_message(encrypted_msg, interval):
    # Extract every nth character from the encrypted message
    decrypted_msg = encrypted_msg[::interval]
    return decrypted_msg

# Encrypt a message
user_message = input("Enter a message to encrypt: ")
result, interval = encrypt_message(user_message)

# Show the encrypted results
print(f"Encrypted message: {result}")
print(f"Interval used: {interval}")

# Decrypt the message
decrypted_message = decrypt_message(result, interval)

# Show the decrypted message
print(f"Decrypted message: {decrypted_message}")
