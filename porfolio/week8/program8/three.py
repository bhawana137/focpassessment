''' The Unixgrepcommand searches a file and outputsthe lines in the file that
 contain a certain pattern. Write an implementation of this. It will take two
 command-line arguments: the first is the string to look for, and the second is the
 file name. The output should be the lines in the file that contain the string. '''
import sys

def grep_command(search_string, file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Iterate through the lines and print those that contain the search string
        found = False
        for line_number, line in enumerate(lines, start=1):
            if search_string in line:
                found = True
                print(f"{line_number}: {line.strip()}")

        if not found:
            print(f"No lines containing '{search_string}' were found in {file_name}.")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Check if both arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python three.py <search_string> <file_name>")
    else:
        # Get the search string and file name from the arguments
        search_string = sys.argv[1]
        file_name = sys.argv[2]
        grep_command(search_string, file_name)
