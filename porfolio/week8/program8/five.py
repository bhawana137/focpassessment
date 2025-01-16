'''  The Unixspellcommand is a simple spell-checker.It prints out all the words in a
 text file that are not found in a dictionary. Write and test an implementation of this,
 that takes a file name as a command-line argument.
 Note: You may want to simplify the program at first by testing with a text file that
 does not contain any punctuation. A complete version should obviously be able to
 handle normal files, with punctuation.
 Another Note: You will need a list of valid words. Linux users will already have one
 (probably in /usr/share/dict/words). It is more complicated,as usual, for
 Windows users. Happily, there are several available on GitHub. '''
import sys
import re

def load_dictionary(dictionary_file):
    """Load the dictionary file into a set of valid words."""
    try:
        with open(dictionary_file, 'r') as file:
            dictionary = set(word.strip().lower() for word in file)
            print("Loaded dictionary:", dictionary)  # Debugging: Confirm dictionary loaded correctly
            return dictionary
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while loading the dictionary: {e}")
        sys.exit(1)

def spell_check(file_name, dictionary):
    """Check the file for misspelled words."""
    try:
        with open(file_name, 'r') as file:
            text = file.read()

        # Remove punctuation and split words
        words = re.findall(r'\b\w+\b', text.lower())
        print("Words extracted from file:", words)  # Debugging: Confirm words extracted correctly

        # Find words not in the dictionary
        misspelled = [word for word in words if word not in dictionary]

        if misspelled:
            print("Misspelled words:")
            for word in sorted(set(misspelled)):
                print(word)
        else:
            print("No misspelled words found.")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python five.py <file_name> <dictionary_file>")
    else:
        file_name = sys.argv[1]
        dictionary_file = sys.argv[2]
        dictionary = load_dictionary(dictionary_file)
        spell_check(file_name, dictionary)
