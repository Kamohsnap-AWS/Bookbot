from stats import *

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_contents = get_book_text(file_path)
    word_count = get_word_count(book_contents)
    character_dict = get_char_count(book_contents)
    print_report(word_count, character_dict)

def get_book_text(path):
    # Opens book and returns the contents
    with open(path) as f:
        return f.read() 

main()
