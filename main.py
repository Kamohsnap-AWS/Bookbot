def main():
    # Used to open book and stores the contents
    with open("Books/frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)





main()