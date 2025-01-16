from PyPDF2 import PdfReader


def read_book(file_path: str) -> str:
    try:
        if file_path.endswith('.pdf'):
            with open(file_path, "rb") as file:
                pdf = PdfReader(file)
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                return text
        elif file_path.endswith('.txt'):
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            print(f"Unsupported file format: {file_path}")
            return ""
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return ""

def get_word_count(book_content: str) -> int:
    words = book_content.split()
    return len(words)


def get_word_frequencies(book_content: str) -> dict:
    words = book_content.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def get_most_common_word(word_counts: dict) -> str:
    return max(word_counts, key=word_counts.get)


def get_least_common_word(word_counts: dict) -> str:
    return min(word_counts, key=word_counts.get)


def main() -> None:
    book_path = "/Users/randydevries/workspace/github.com/FREEZLER/bookbot/books/allShakespeare.txt"
    book_content = read_book(book_path)

    if book_content is not None:
        word_count = get_word_count(book_content)
        word_count_message = f"The book has {word_count} words"
        word_frequencies = get_word_frequencies(book_content)
        most_common_word = get_most_common_word(word_frequencies)
        least_common_word = get_least_common_word(word_frequencies)

        print("\n" + "*-----------------------------*")
        print(f"*{book_path.split('/')[-1].center(29)}*")
        print("*-----------------------------*")
        print(f"*{word_count_message.lower().center(29)}*")
        print(f"*{('Number of vowels: ' +
              str(sum(1 for char in book_content.lower() if char in 'aeiou'))).center(29)}*")
        print(f"*{('Most common: ' + most_common_word).center(29)}*")
        print(f"*{('Least common: ' + least_common_word).center(29)}*")
        print("*-----------------------------*\n")
    else:
        print("*-----------------------------*")
        print("* Failed to read the book.    *")
        print("*-----------------------------*")


if __name__ == "__main__":
    main()
