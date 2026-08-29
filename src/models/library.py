class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def add_member(self, member):
        self.members.append(member)
    
    def add_loan(self, loan):
        if not loan.book in self.books:
            print("Book is not in the library.")
            return
        if not loan.member in self.members:
            print("Member is not registered.")
            return
        if len(self.find_loans_by_member(loan.member)) >= 3:
            print("Member has reached the borrowing limit.")
            return
        if not loan.book.available:
            print("Book is already borrowed.")
            return
        loan.book.borrow()
        self.loans.append(loan)
        
    def remove_book(self, book):
        self.books.remove(book)
    
    def remove_member(self, member):
        self.members.remove(member)
        
    def return_book(self, loan):
        if not loan.book.available:
            self.loans.remove(loan)
        loan.book.return_book()
        
    def find_book(self, isbn):
        for book in self.books:
            if book.ISBN == isbn:
                return book
        print("Book not found.")
            
    def find_member(self, ID):
        for member in self.members:
            if member.member_ID == ID:
                return member
        print("Member not found.")
        
    def display_info(self):
        print("#Books:")
        for book in self.books:
            print(book)
        print("#Members:")
        for member in self.members:
            print(member)
        print("#Loans:")
        for loan in self.loans:
            print(loan)
    
    def find_loan_by_book(self, book):
        for loan in self.loans:
            if loan.book == book:
                return loan
        print("Loan not found.")

    def find_loans_by_member(self, member):
        member_loans = []
        for loan in self.loans:
            if loan.member == member:
                member_loans.append(loan)
        return member_loans
    