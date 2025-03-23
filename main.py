import sys
from stats import word_count
from stats import character_count
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path} ...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(text)} total words")
    print("--------- Character Count -------")
    characters = character_count(text)
    sorted_chars = sort_dictionary(characters)
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

main()