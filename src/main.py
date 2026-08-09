from models.book import Book
from models.member import Member
from models.loan import Loan
def main():
    book = Book(
        "Clean Code",
        "Robert C.Martin",
        "9780132350884"
    )
    book.display_info()
    book.borrow()
    
    book.display_info()
    
    book.borrow()
    book.return_book()
    
    book.display_info()
    
    book.return_book()
    
    member = Member("Shokat", 103)
    member.display_info()
    
    loan = Loan(book, member, "2026-08-09", "2026-08-23")
    loan.display_info()
    
    
if __name__ == "__main__":
    main()