''' Modify the previous program so that it can process any numberof values. The input
 terminates when the user just pressed "Enter" at the prompt rather than entering a
 value '''

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  

# List to store temperatures in Fahrenheit
fahrenheit_temps = []

# Loop to read temperatures until the user presses Enter without input
while True:
    temp_input = input("Enter a temperature in Celsius or press Enter to finish: ")
    
    # If the user presses Enter without typing anything, stop the loop
    if temp_input == "":
        break
    
    # Check if the input ends with 'C'
    if temp_input[-1].upper() == 'C':
        celsius = float(temp_input[:-1])  # Remove 'C' and convert the number to float
        fahrenheit = celsius_to_fahrenheit(celsius)  
        fahrenheit_temps.append(fahrenheit)  # Add to the list
    else:
        print("Invalid input. Please enter the temperature followed by 'C'.")

# If there are temperatures in the list, calculate and display the results
if fahrenheit_temps:
    max_temp = max(fahrenheit_temps)  
    min_temp = min(fahrenheit_temps)  
    mean_temp = sum(fahrenheit_temps) / len(fahrenheit_temps)  
    print("\nResults:")
    print(f"Maximum temperature: {max_temp}°F")
    print(f"Minimum temperature: {min_temp}°F")
    print(f"Mean temperature: {mean_temp}°F")
else:
    print("No temperatures were entered.")
