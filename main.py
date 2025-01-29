def main():
    file_path = "Books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    num_words = get_word_count(book_contents)
    char_dict = get_char_count(book_contents)

    print_report(num_words, char_dict)

def get_book_text(path):
    # Opens book and returns the contents
    with open(path) as f:
        return f.read()

def get_word_count(text):
    # Returns the number of words in our current book
    return len(text.split())    

def get_char_count(text):
    # Keeps track of the count of every character that appears in the text
    chars = {}
    
    # Initializes characters not in dictonary with value of 1.
    # Increments character counter by 1 if already in dictionary.
    for ch in text.lower():
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1

    return chars

def print_report(w_count, c_dict):
    print("--- Begin Report ---")
    print(f"{w_count} words were found in the document\n")

    # Prints all the alphabetical characters and the number of times they appear
    for key in c_dict:
        if key.isalpha():
            print(f"The '{key}' character was found {c_dict[key]} times")

    print("\n--- End Report ---")

main()