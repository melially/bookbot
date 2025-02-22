from stats import get_num_words
from stats import character_count
import sys
print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    file = sys.argv[1]

    sys.argv

    get_book_text(file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    get_num_words(get_book_text(file))
    character_count(file)
    print("============= END ===============")

main()