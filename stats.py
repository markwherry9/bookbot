def word_count(text):
    word_list = text.split()
    return len(word_list)

def character_count(text):
    text = text.lower()
    char_count = {}
    for c in text:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_dictionary(my_dict):
    dict_list = []
    for k, v in my_dict.items():
        dict_list.append([k, v])
    return sorted(dict_list, key = lambda x: int(x[1]), reverse = True)
