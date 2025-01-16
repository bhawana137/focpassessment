''' The Unixdiffcommand compares two files and reportsthe differences, if any.
 Write a simple implementation of this that takes two file names as command-line
 arguments and reports whether or not the two files are the same. (Define "same" as
 having the same contents.) '''


import sys

def diff_command(file1, file2):
    try:
        # Open and read the contents of both files
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            file1_lines = f1.readlines()
            file2_lines = f2.readlines()

        # Compare the contents of both files
        if file1_lines == file2_lines:
            print("The files are the same.")
        else:
            print("The files are different.")
            
            # Report differences line by line
            for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines), start=1):
                if line1 != line2:
                    print(f"Difference at line {i}:")
                    print(f"  File1: {line1.strip()}")
                    print(f"  File2: {line2.strip()}")

            # Handle extra lines in either file
            if len(file1_lines) > len(file2_lines):
                print("Extra lines in File1:")
                for line in file1_lines[len(file2_lines):]:
                    print(f"  {line.strip()}")
            elif len(file2_lines) > len(file1_lines):
                print("Extra lines in File2:")
                for line in file2_lines[len(file1_lines):]:
                    print(f"  {line.strip()}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Check if both file names are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python two.py <file1> <file2>")
    else:
        # Get the file names from the arguments
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        diff_command(file1, file2)
