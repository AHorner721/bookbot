from stats import count_words, count_characters, sort_book_data
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    count_words(book_text)
    print("--------- Character Count -------")
    character_count = count_characters(book_text)
    sort_book_data(character_count)
    print("============= END ===============")

main()