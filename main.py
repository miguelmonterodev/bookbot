def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_content = f.read()
    return file_content

def main():
    num_words = len(get_book_text("books/frankenstein.txt").split())
    print(f"{num_words} words found in the document")

main()