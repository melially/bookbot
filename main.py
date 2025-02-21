def wordcount(source):
    count = len(source.split())
    print(f"{count} words found in the document")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        #print(file_contents)
        wordcount(file_contents)

def main():
    get_book_text("books/frankenstein.txt")


main()