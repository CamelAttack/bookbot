def get_word_count(book_text):
    book_words = book_text.split()
    return len(book_words)

def get_letter_count(book_text):
    letter_count_dictionary = {}
    lower_case_text = book_text.lower()
    for character in lower_case_text:
        if character in letter_count_dictionary:
            letter_count_dictionary[character] = letter_count_dictionary[character]+1
        else:
            letter_count_dictionary[character] = 1
    return letter_count_dictionary


def print_character_report(char_count_dictionary):
    print("--------- Character Count -------")
    for char in sorted(char_count_dictionary, key=char_count_dictionary.get, reverse=True):
        if char.isalpha():
            print(f"{char}: {char_count_dictionary[char]}")
    return