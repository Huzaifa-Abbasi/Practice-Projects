'''Question 2: Library Book Reservation System
Design a Python program for a Library Book Reservation System. Create a function 
reserve_book(book_title, student_status) that allows students to reserve a book. If the book is available 
and the student is a regular student, reserve the book; if the student is a VIP student, provide instant 
reservation. Handle cases where the book is not available.'''

def reserve_book(book_title, student_status):
    return book_title, student_status

book_shelf = ["maths", "english"]

book_title = input("Enter the Book Title ").lower()

student_status = input("Enter the status of student (regular/vip): ").lower()

if book_title in book_shelf and student_status == "regular":
    print("Book is available", reserve_book(book_title, student_status))
elif book_title in book_shelf and student_status == "vip":
    print("Instant reservation for VIP student")
else:
    print("Book not available for the specified status")