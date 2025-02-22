from stats import get_num_words
from stats import character_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        #print(file_contents)
        #get_num_words(file_contents)
        return file_contents

def main():
    file = "books/frankenstein.txt"

    get_book_text(file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    get_num_words(get_book_text(file))
    character_count(file)
    
    #print(file_contents)
    #/ne: 44538
    #/nt: 29493
    print("============= END ===============")
#"""
main()