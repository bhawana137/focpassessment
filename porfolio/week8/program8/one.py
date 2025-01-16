''' The Unixnlcommand prints the lines of a text filewith a line number at the start
 of each line. (It can be useful when printing out programs for dry runs or white-box
 testing). Write an implementation of this command. It should take the name of the
 files as a command-line argument. '''

import sys

def nl_command(file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Iterate through the lines and print those that are not empty
        for line_number, line in enumerate(lines, start=1):
            if line.strip():  # Skip lines that are empty or only contain whitespace
                print(f"{line_number:>6}  {line.strip()}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Check if the file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python one.py <file_name>")
    else:
        # Get the file name from the arguments
        file_name = sys.argv[1]
        nl_command(file_name)

