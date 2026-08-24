class Member:
    def __init__(self, name, member_ID):
        self.name = name
        self.member_ID = member_ID
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_ID}")
   
    def __str__(self):
        return self.name