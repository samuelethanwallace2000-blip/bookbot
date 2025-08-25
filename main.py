import sys
from stats import get_num_words, get_char_count, sort_on 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    
    book_text = get_book_text(book_path)
    
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    char_count = get_char_count(book_text)
    sorted_chars = sort_on(char_count)
    for char, count in sorted_chars.items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()