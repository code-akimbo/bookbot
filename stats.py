

def anylize_book(file):
    with open(file) as f:
        book = f.read()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}")
        print("----------- Word Count ----------")
        print(f"Found {book_words(book)} total words")
        print("--------- Character Count -------")
        print(book_letters(book))
        print("============= END ===============")
        

def book_words(book):
    word_count = book.split()
    return len(word_count)


def book_letters(book):
    letter_dict = create_letter_dict(book)
    letter_list = create_letter_list(letter_dict)
    formatted_list = create_formatted_list(letter_list)
    return formatted_list


def create_letter_dict(book):
        
    character_dict = {}
    for i in book:
        if i.lower() in character_dict and i.isalpha():
            character_dict[i.lower()] += 1
        elif i.lower() not in character_dict and i.isalpha():
            character_dict[i.lower()] = 1
        else:
            pass

    return character_dict


def create_letter_list(letter_dict):
    character_list = []
    for i in letter_dict:
        character_list.append({"letter": i, "value": letter_dict[i]})

    character_list.sort(reverse=True, key=sort_on)

    return character_list


def create_formatted_list(letter_list):
    formatted_list = ""
    for i in letter_list:
        formatted_list += f"{i["letter"]}: {i["value"]}\n"
    return formatted_list


def sort_on(items):
    return items["value"]
