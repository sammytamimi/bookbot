from stats import word_counter, char_counter, sort_char_counter
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
    
open_book = get_book_text(book_path)

char_list = char_counter(open_book)

sorted_chars = sort_char_counter(char_list)

def pretty_report(list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(open_book)} total words")
    print("--------- Character Count -------")
    for dict_item in list:
        print(f"{dict_item['char']}: {dict_item['num']}")
        
        

    

def main():
    book = get_book_text(book_path)
    return book




pretty_report(sorted_chars)




    
    
    

