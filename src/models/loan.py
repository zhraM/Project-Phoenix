class Loan:
    def __init__(self, book, member, borrow_date, due_date):
        self.book = book
        self.member = member
        self.borrow_date = borrow_date
        self.due_date = due_date
        
    def display_info(self):
        print(f"Book: {self.book}")
        print(f"Member: {self.member}")
        print(f"Borrow Date: {self.borrow_date}")
        print(f"Due Date: {self.due_date}")