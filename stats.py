def get_word_count(text):
    # Splits the string of text to returns the current number of words
    return len(text.split())

def get_char_count(text):
    # Keeps track of the count of every character that appears in the text
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_chars(chars):
    # Converts chars dict to a list of valid key-value pairs
    chars_list = [[key, values] for key, values in chars.items() if key.isalpha()]
    # We want our items stored largest to smallest
    sorted_chars = sorted(chars_list, key=lambda x: x[1], reverse=True)
    return sorted_chars  

def print_report(w_count, chars):
    print("--- Begin Report ---")
    print(f"{w_count} words found in the document\n")
    sorted_chars = sort_chars(chars)
    
    for char in sorted_chars:
        print(f"'{char[0]}: {char[1]}'")

    print("\n--- End Report ---")
