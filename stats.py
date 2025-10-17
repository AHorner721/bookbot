def count_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def count_characters(text):
    char_count_dict = {}
    for character in text:
        character = character.lower()
        if(character in char_count_dict):
            char_count_dict[character] += 1
        else:
            char_count_dict[character] = 1
    return char_count_dict

def sort_on(items):
    return items["num"]

def sort_book_data(char_dict):
    dict_list = []
    for char in char_dict:
        new_dict = {"char": char, "num": char_dict[char]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    for item in dict_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
