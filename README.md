# oop_assignment_1
README.md # This file
procedural_version/
library_procedural.py # Procedural version of the library system
test_procedural.py # Tests for the procedural version
oop_solution/
library_oop.py # Object-Oriented Programming (OOP) version
test_oop.py # Tests for the OOP version

Book
attributes:bookid,title,author,total_copies
Member
attributes:memberid,name,email,borrowed->list
library
attributes:books,members

Basic Operations
-Adding books and members
-Borrowing and returning books
-Displaying information

How to Run Tests
1 Copy `oop_solution/` or `procedural_version/` to your working directory.
2 Run the associated test file:
   python test_oop.py
    or
   python test_procedural.py