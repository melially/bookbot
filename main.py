from stats import get_num_words
from stats import character_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        #print(file_contents)
        get_num_words(file_contents)

def main():
    get_book_text("books/frankenstein.txt")
    character_count("books/frankenstein.txt")


main()