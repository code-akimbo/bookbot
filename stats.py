

def anylize_book(file):
    with open(file) as f:
        file_contents = f.read()
        print(count_book_words(file_contents))
        print(count_book_characters(file_contents))


def count_book_words(book):
    word_count = book.split()
    return f"{len(word_count)} words found in the document"


def count_book_characters(book):
    character_dict = {}

    for i in book:
        if i.lower() in character_dict:
            character_dict[i.lower()] += 1
        else:
            character_dict[i.lower()] = 1
    
    return character_dict


def sort_character_dict():
    character_dict = count_book_characters(book)