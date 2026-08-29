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
    library.add_loan(loan)
    
    library.return_book(loan)
    print(book.available)
    print(library.loans)
    library.return_book(loan)
    library.add_loan(loan)
    
    book1 = Book(
        "Just for check",
        "No One",
        "6273874983903"
    )
    member1 = Member("Zizi", 450)
    loan1 = Loan(book1, member, "2026-08-09", "2026-08-23")
    loan2 = Loan(book, member1, "2026-08-09", "2026-08-23")
    library.add_loan(loan1)
    library.add_loan(loan2)

    found_book = library.find_book("9780132350884")
    print(found_book)
    found_member = library.find_member(103)
    print(found_member)
    library.find_book("111111")
    library.find_member(999)
    
    library.display_info()
    
    print(library.find_loan_by_book(book))
    loans = library.find_loans_by_member(member)
    for loan in loans:
        print(loan)
        
        
    book2 = Book(
        "Become SuperNatural",
        "Joe Dispenza",
        "98376473292"
    )
    book3 = Book(
        "The Hunger Games",
        "Suzanne Collins",
        "87882767298"
    )
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    loan2 = Loan(book2, member, "2026-8-26", "2026-9-10")
    loan3 = Loan(book3, member, "2026-8-26", "2026-9-10")
    library.add_loan(loan1)
    library.add_loan(loan2)
    library.add_loan(loan3)
    loans = library.find_loans_by_member(member)
    for loan in loans:
            print(loan)
    
    
    
if __name__ == "__main__":
    main()