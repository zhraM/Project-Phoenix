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
        if loan.book.available:
            self.loans.append(loan)
        loan.book.borrow()
        
    def remove_book(self, book):
        self.books.remove(book)
    
    def remove_member(self, member):
        self.members.remove(member)
        
    def return_book(self, loan):
        if not loan.book.available:
            self.loans.remove(loan)
        loan.book.return_book()
        
        
        
        