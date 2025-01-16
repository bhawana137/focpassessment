''' Write a program that manages a list of countries and their capital cities. It should
 prompt the user to enter the name of a country. If the program already "knows"
 the name of the capital city, it should display it. Otherwise it should ask the user to
 enter it. This should carry on until the user terminates the program (how this
 happens is up to you). '''

def manage_countries():
    # Dictionary to store country and capital pairs
    countries_and_capitals = {}

    while True:
        # Prompt the user to enter a country or 'exit' to quit
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip()

        # Allow the user to exit the program
        if country.lower() == 'exit':
            print("End")
            break

        # Standardize input to lowercase to handle case insensitivity
        country = country.lower()

        # Check if the country is already in the dictionary
        if country in countries_and_capitals:
            print(f"The capital of {country.title()} is {countries_and_capitals[country]}.")
        else:
            # If the country is not in the dictionary, ask for its capital
            capital = input(f" The capital of {country.title()} is : ").strip()
            # Add the country and its capital to the dictionary
            countries_and_capitals[country] = capital
            print(f"The capital of {country.title()} has been added.")

# Run the program
manage_countries()
