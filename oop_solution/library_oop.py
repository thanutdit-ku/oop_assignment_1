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
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    def __str__(self):
        return f"{self.title} by {self.author} - {self.available_copies}/{self.total_copies} available"
class Member():
    def __init__(self,memberid,name,email):
        self.memberid = memberid
        self.name = name
        self.email = email
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            return False
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False
    def return_book(self, book):
        if book not in self.borrowed_books:
            return False
        book.return_book()
        self.borrowed_books.remove(book)
        return True
    def list_borrowed_books(self):
        return self.borrowed_books
    
    def __str__(self):
        if not self.borrowed_books:
            return f"{self.name} (No books borrowed)"
        books_list = "\n  ".join(str(book) for book in self.borrowed_books)
        return f"{self.name} borrowed:\n  {books_list}"

   
class Library():
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, book_id, title, author, copies):
        book = Book(book_id, title, author, copies)
        self.books[book_id] = book
        return f"Book '{title}' added successfully!"
    
    def add_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        self.members[member_id] = member
        return f"Member '{name}' registered successfully!"
    
    def find_book(self, book_id):
        return self.books.get(book_id)
    
    def find_member(self, member_id):
        return self.members.get(member_id)
    
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False

        if not member.borrow_book(book):
            print("Error: Cannot borrow (limit reached or no copies left)")
            return False
        print(f"{member.name} borrowed '{book.title}'")
        return True    
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False
        if not member.return_book(book):
            print("Error: This member hasn't borrowed this book!")
            return False
        print(f"{member.name} returned '{book.title}'")
        return True
    
    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books.values():
            if book.available_copies > 0:
                print(book)
    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book in member.borrowed_books:
                print(f"- {book.title} by {book.author}")