'''  Write a program that reads 6 temperatures (in the same format as before), and
 displays the maximum, minimum, and mean of the values.  '''

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  

# List to store temperatures in Fahrenheit
fahrenheit_temps = []

# Read 6 temperatures in Celsius
for i in range(6):
    temp_input = input(f"Enter temperature {i+1} in Celsius: ")
    
    # Check if the input ends with 'C'
    if temp_input[-1].upper() == 'C':
        celsius = float(temp_input[:-1])  # Remove 'C' and convert the number to float
        fahrenheit = celsius_to_fahrenheit(celsius)  
        fahrenheit_temps.append(fahrenheit)  # Add to the list
    else:
        print("Invalid input. Enter the temperature followed by 'C'.")
        break  # Stop if invalid input is entered

# If all inputs are valid, calculate and display the results
if len(fahrenheit_temps) == 6:
    max_temp = max(fahrenheit_temps)  
    min_temp = min(fahrenheit_temps)  
    mean_temp = sum(fahrenheit_temps) / len(fahrenheit_temps)  

    print("\nResults:")
    print(f"Maximum temperature: {max_temp}°F")
    print(f"Minimum temperature: {min_temp}°F")
    print(f"Mean temperature: {mean_temp}°F")
