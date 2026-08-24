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
        