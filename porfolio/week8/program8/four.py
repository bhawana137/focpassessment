''' The Unixwccommand counts the number of lines, words,and characters in a file.
 Write an implementation of this that takes a file name as a command-line
 argument, and then prints the number of lines and characters.
 Note: Linux (and Mac) users can use the "wc" commandto check the results of their
 implementation. '''
import sys

def wc_command(file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Count lines and characters
        line_count = len(lines)
        char_count = sum(len(line) for line in lines)

        # Print the results
        print(f"Number of ines: {line_count}")
        print(f"Number of characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Check if the file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python four.py <file_name>")
    else:
        # Get the file name from the arguments
        file_name = sys.argv[1]
        wc_command(file_name)
