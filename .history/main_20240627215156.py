def read_book(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None


def count_words(book):
    words = book.split()
    num_words = len(words)
    return num_words


def main():
    book_path = "/Users/randydevries/workspace/github.com/FREEZLER/bookbot/books/frankenstein.txt"
    book = read_book(book_path)

    if book is not None:
        _extracted_from_main_(book)
    else:
        print("Failed to read the book.")


# TODO Rename this here and in `main`
def _extracted_from_main_(book):
    num_words = count_words(book)
    my_string = f"The book has {num_words} words."
    lowered_string = book
    print(my_string.lower())

    number_of_vowels = sum(char in "aAeEiIoOuU" for char in lowered_string)
    print(f"Number of vowels: {number_of_vowels}")


# check if the script is being run directly if not import it!
if __name__ == "__main__":
    main()

