from stats import get_num_words, count_words, sort_on, sorted_list
import sys

def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        content = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(get_num_words(content))
        print("--------- Character Count -------")
        new_list = sorted_list(count_words(content))
        for item in new_list:
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")


main()