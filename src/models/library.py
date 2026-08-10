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
        self.loans.append(loan)
        
    def remove_book(self, book):
        self.books.remove(book)
    
    def remove_member(self, member):
        self.members.remove(member)