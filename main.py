def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = word_count(text)
    print(text)
    print(total_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

main()