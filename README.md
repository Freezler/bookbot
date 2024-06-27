# Welcome to BookBot

### A Python program that can analyze an entire book and print out an interesting statistical report.

The code reads a book from a file, counts the number of words and vowels in the book, and prints the results.

**Functionality:**

- **Reading a Book:**
  The program reads the content of a book from a file. This is achieved by passing the file path to the `read_book` function.

- **Counting Words:**
  It counts the number of words in the book. This process starts immediately after the book is read from the specified file.

- **Analyzing Vowels:**
  The text of the book is converted to lowercase to ensure consistency during the analysis. Subsequently, the program counts the number of vowels in the lowercase text.

- **Generating Report:**
  The final report includes the total number of words and vowels found in the text of the book.

**Parameters:**

- `file_path`: A string that represents the file path to the text file containing the book. The `read_book` function uses this parameter to access and read the contents of the file.

**Execution:**

The `main()` function orchestrates the execution of the program. It is responsible for reading the book from the specified file path, counting the words, converting the text to lowercase, counting the vowels, and printing the final statistical report. This function is executed when the script is run directly.