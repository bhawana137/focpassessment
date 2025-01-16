'''Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.'''
import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: python four.py <URL>")
        return

    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} is not working. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not reach the website at {url}. Details: {e}")

if __name__ == "__main__":
    main()
