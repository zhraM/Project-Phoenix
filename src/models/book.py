class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True
    
    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Status: {status}")
        
    def borrow(self):
        if not self.available:
            print("Book is already borrowed.")
        else:
            self.available = False
    
    def return_book(self):
        if self.available:
            print("Book is already available.")
        else:
            self.available = True