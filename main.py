from stats import get_word_count
from stats import get_letter_count
from stats import print_character_report
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_string = file.read()
        return file_string
    
def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = arguments[1]
    book_text = get_book_text(book_file)
    word_count = get_word_count(book_text)
    letter_count_dictionary = get_letter_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print_character_report(letter_count_dictionary)
    print("============= END ===============")
    return

main()