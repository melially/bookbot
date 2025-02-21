#get_book_text function; takes file path, returns contents as string
"""
with open(path_to_file) as f:
    # do something with f (the file) here

To turn into string
# f is a file object
file_contents = f.read()
"""
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)

#main function that uses above w/ /relative/ path to txt to print to console

def main():
    get_book_text("books/frankenstein.txt")
#call main
main()
"""

asdasd
"""