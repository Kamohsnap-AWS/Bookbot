def get_word_count(text):
    # Splits the string of text to returns the current number of words
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
    print(f"{w_count} words found in the document\n")

    # Prints all the alphabetical characters and the number of times they appear
    for key in sorted(c_dict):
        if key.isalpha():
            print(f"The '{key}' character was found {c_dict[key]} times")

    print("\n--- End Report ---")
