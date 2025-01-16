''' Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used. '''
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("Usage: python os_platform_report.py\n"
              "This program reports the operating system platform being used.")
    else:
        print(f"Operating System Platform: {sys.platform}")

if __name__ == "__main__":
    main()
