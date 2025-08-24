from stats import get_num_words, count_words, sort_on, sorted_list

def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_content = f.read()
    return file_content

def main():
    content = get_book_text("books/frankenstein.txt")
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