def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    char_count = {}
    for i in text:
        i = i.lower()
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def get_sorted_char(characters):
    char_list = []
    for character in characters:
        char_list.append({"char": character, "num": characters[character]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    