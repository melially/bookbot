def get_num_words(source):
    count = len(source.split())
    print(f"{count} words found in the document")


"""
    Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
        Convert any character to lowercase using the .lower() method, we don't want duplicates.
        Use a dictionary of String -> Integer. The returned dictionary should look something like this:

{'p': 6121, 'r': 20818, 'o': 25225, ...
"""
def character_count(source):
    with open(source) as f:
        file_contents = str.lower(f.read())
        char_count = {}
        for i in file_contents:
            if i in char_count:
                char_count[i.lower()] = char_count[i.lower()] + 1
            else:
                char_count[i.lower()] = 1
        print(char_count)
        