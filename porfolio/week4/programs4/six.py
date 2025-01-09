'''  Write a program that takes a centigrade temperature and displays the equivalent in
 fahrenheit. The input should be a number followed by a letter C. The output should
 be in the same format. '''

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32  
    return fahrenheit

# Get the input from the user (e.g., 25C)
temp_input = input("Enter the temperature in Celsius: ")

# Remove the 'C' at the end and convert the remaining part to a float
if temp_input[-1].upper() == 'C':
    celsius = float(temp_input[:-1])  # Convert string to float, excluding the 'C'
    fahrenheit = celsius_to_fahrenheit(celsius)  
    print(f"{fahrenheit}F")  
else:
    print("Invalid input. Enter the temperature followed by 'C'.")
