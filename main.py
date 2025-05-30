from stats import count_words, count_letters, sort_dict
import sys

def main():
    # if filepath is not passed in, print an error message to console
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # otherwise continue as normal
    target_file = sys.argv[1]
    book_text = get_book_text(target_file)
    num_words = count_words(book_text)
    letter_dict = count_letters(book_text)
    sorted_list = sort_dict(letter_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {target_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # for each entry in the dictionary list of characters and counts,
    for i in range(0, len(sorted_list)):
        current_entry = sorted_list[i]
        # evaluate if it is an alphabetical character
        if current_entry['char'].isalpha():
            # and if so, print it and the number of times it occurs
            print(f"{current_entry['char']}: {current_entry['count']}")
    print("============= END ===============")

def get_book_text(filepath):
    # open the file containing a book at filepath
    with open(filepath) as book:
        # read the contents of the book into a string
        return book.read()

main()