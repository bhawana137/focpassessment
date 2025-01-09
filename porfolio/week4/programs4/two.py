'''  Write a function that has a single string as its parameter, and returns the number of
 uppercase letters, and the number of lowercase letters in the string. Test the
 function with a short program. '''

# Function to count uppercase and lowercase letters
def count_case(s):
    # Start counters at 0
    uppers = 0
    lowers = 0

    # loop for each character in the string
    for letter in s:
        if letter.isupper():  # Check if it's uppercase
            uppers += 1
        elif letter.islower():  # Check if it's lowercase
            lowers += 1

    return uppers, lowers  

# Test the function
print("Testing the function ")

# Trying it with a sample sentence
test_string = "Hi! I am Bhawana Shrestha"
up, low = count_case(test_string)  

print("String:", test_string)
print("Number of uppercase letters:", up)
print("Number of lowercase letters:", low)
