''' One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
 to identify the language used, and sometimes some of the letters. In English, the
 most common letter is "e", and so the symbol representing "e" should appear most
 in the encrypted text. Write a program that processes a string representing a message and reports the six
 most common letters, along with the number of times they appear. Case should
 not matter, so "E" and "e" are considered the same.'''

def freq_analysis(message):
    # Initialize a dictionary to store letter frequencies
    letter_count = {chr(i): 0 for i in range(97, 123)}  # Dictionary for a-z with initial count 0

    # Process each letter in the message
    for char in message.lower():
        if char.isalpha():  # Only count alphabetic characters
            letter_count[char] += 1

    # Sort the dictionary by frequency (in descending order) and get the top 6
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)[:6]

    # Print the results
    print("The six most common letters are:")
    for letter, count in sorted_letters:
        print(f"{letter.upper()}: {count}")

# Test the function
message = input("Enter an encrypted message: ")
freq_analysis(message)
