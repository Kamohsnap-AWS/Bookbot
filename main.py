import sys, os
from stats import *

def main():
    verify_arg_count()
    file_path = sys.argv[1]
    verify_valid_args(file_path)

    book_contents = get_book_text(file_path)
    word_count = get_word_count(book_contents)
    character_dict = get_char_count(book_contents)
    print_report(word_count, character_dict)

def verify_arg_count():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
def verify_valid_args(path):
    if not os.path.exists(path):
        print("The given <path_to_book> does not exist in our library. Enter a valid <path_to_book>.")
        sys.exit(1)

def get_book_text(path):
    # Opens book and returns the contents
    with open(path) as f:
        return f.read() 

main()
