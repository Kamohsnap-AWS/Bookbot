def main():
    # Used to open book and stores the contents
    with open("Books/frankenstein.txt") as f:
        file_contents = f.read()

    print(get_word_count(file_contents))
    
    print(get_char_count(file_contents))

# Counts the number of words in our current book
def get_word_count(text):
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



main()