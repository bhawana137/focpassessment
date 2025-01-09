'''  When processing data it is o en useful to remove the last character from some
 input (it is o en a newline). Write and test a function that takes a string parameter
 and returns it with the last character removed. (If the string contains one or fewer
 characters, return it unchanged.) '''

# Function to remove the last character from a string
def remove_last_char(s):
    if len(s) > 1:  # Check if the string is longer than 1 character
        return s[:-1]  # Remove the last character
    return s  

# Test the function
print("Testing the function...")

# Test with different strings
print(remove_last_char("Bhawana"))  
print(remove_last_char("A"))      
print(remove_last_char("Shrestha."))       
  
