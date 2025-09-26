def word_counter(book: str):
    split = book.split()
    num_words = len(split)
    return num_words
    
def char_counter(book: str):
    text = book.lower()
    char_count = {}
    
    for char in text:
        if char in char_count and char.isalpha():
            char_count[char] +=1
        elif char not in char_count and char.isalpha():
            char_count[char] = 1
    
    return char_count

def sort_on(chars):
    return chars["num"]


def sort_char_counter(char_count: dict):
    sorted_list_chars = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    sorted_dict_list = []
    for pair in sorted_list_chars:
        sorted_dict_list.append({"char": pair[0], "num": pair[1]})
        
    return sorted_dict_list
        
    


        
        