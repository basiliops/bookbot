import sys

from stats import (
    get_word_count,
    get_char_count,
    get_sorted_char,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_list = get_sorted_char(char_count)
    print_report(book_path, word_count, char_list)

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return book_contents

def print_report(book_path, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()