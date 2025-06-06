def count_words(book):
    # split book into array of words, count them
    return len(book.split())

def count_letters(book):
    # instantiate empty character_counts dictionary to be filled
    char_counts = {}
    # loop through every characher in the text, 1 by 1
    for char in book.lower():
        # if dictionary entry exists for character, increment
        if char in char_counts:
            char_counts[char] += 1
        # otherwise instantiate dictionary entry for character
        else:
            char_counts[char] = 1
    return char_counts

def sort_dict(char_dict):
    # make a new list to hold dictionary entries for each character and it's count
    char_list = []
    for char, count in char_dict.items():
        # append a new dictionary entry to the list for each character present; {char: "char", count: "count"}
        char_list.append({"char": char, "count": count})
    # sort the list from most common to least common character
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list