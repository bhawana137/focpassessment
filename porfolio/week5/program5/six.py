'''Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.'''
import sys
import shutil

def main():
    if len(sys.argv) != 2:
        print("Usage: python six.py <filename>")
        return

    original_file = sys.argv[1]
    backup_file = original_file + ".bak"

    try:
        shutil.copy(original_file, backup_file)
        print(f"Backup created: {backup_file}")
    except FileNotFoundError:
        print(f"Error: The file '{original_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{original_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
