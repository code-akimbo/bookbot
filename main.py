import sys
from stats import anylize_book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        anylize_book(sys.argv[1])


main()