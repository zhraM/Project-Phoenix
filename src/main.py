from models.book import Book
from models.member import Member
from models.loan import Loan
from models.library import Library
def main():
    #Book
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
    
    #Member
    member = Member("Shokat", 103)
    member.display_info()
    
    #Loan
    loan = Loan(book, member, "2026-08-09", "2026-08-23")
    loan.display_info()
    
    #Library
    library = Library()
    library.add_book(book)
    library.add_member(member)
    library.add_loan(loan)
    print(library.books)
    print(library.members)
    print(library.loans)
    
    
if __name__ == "__main__":
    main()