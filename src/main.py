from models.book import Book

def main():
    book = Book(
        "Clean Code",
        "Robert C.Martin",
        "9780132350884"
    )
    book.display_info()
    
if __name__ == "__main__":
    main()