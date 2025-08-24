
def get_num_words(string):
    num_words = len(string.split())
    return f"Found {num_words} total words"

def count_words(text):
    counter = {}
    for ch in text.lower():
        if ch in counter:
            counter[ch] += 1
        else:
            counter[ch] = 1
    return counter 

def sort_on(items):
    return items["num"]

def sorted_list(dictionary):
    new_list = []
    for key in dictionary:
        new_list.append({"char": key, "num": dictionary[key]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list