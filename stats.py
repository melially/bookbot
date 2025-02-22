def get_num_words(source):
    count = len(source.split())
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

from collections import OrderedDict

def character_count(source):
    with open(source) as f:
        file_contents = str.lower(f.read())
        char_count = {}
        for i in file_contents:
            if i in char_count:
                char_count[i.lower()] = char_count[i.lower()] + 1
            else:
                char_count[i.lower()] = 1
        desc_list = OrderedDict(sorted(char_count.items()))
        ord_list = sorted(desc_list.items(), key=lambda x: x[1], reverse=True)

        print("--------- Character Count -------")
        for key, value in ord_list:
            if key.isalpha(): 
	            print(f"{key}: {value}")

""" The Hint
# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]
vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]

"""