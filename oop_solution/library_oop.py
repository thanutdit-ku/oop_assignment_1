class Book():
    def __init__(self,bookid,title,author,total_copies):
        self.id = bookid
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def returnbook(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
class Member():
    def __init__(self,memberid,name,email):
        self.memberid = memberid
        self.name = name
        self.email = email
        self.borrowed_books_list = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books_list) >= 3:
            return False, "Borrowing limit reached"
        if book.borrow():
            self.borrowed_books.append(book)
            return True, f"{self.name} borrowed '{book.title}'"
        return False, "No copies available"
class Library():
    def __init__(self):
        self.books = []
        self.members = []