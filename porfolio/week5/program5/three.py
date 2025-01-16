''' Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them. '''
import sys

def main():
    if len(sys.argv) <= 1:
        print("No arguments provided. Please provide some arguments.")
        return

    arguments = sys.argv[1:]
    shortest = sorted(arguments, key=len)[0]
    print(f"The shortest argument is: {shortest}")

if __name__ == "__main__":
    main()
