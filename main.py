# Student Library Management System
# Beginner-friendly Python project using OOP

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books available in the library:")
        for book in self.books:
            print(" •", book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued '{bookName}'. Please return it within 30 days.")
            self.books.remove(bookName)
        else:
            print("Sorry, this book is not available right now.")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thank you for returning the book!")

class Student:
    def requestBook(self):
        return input("Enter the book name you want to borrow: ")

    def returnBook(self):
        return input("Enter the book name you want to return: ")

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "CLRS", "Python Notes"])
    student = Student()

    while True:
        print("""
====== Welcome to Central Library ======
1. Display available books
2. Borrow a book
3. Return a book
4. Exit
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            centralLibrary.displayAvailableBooks()
        elif choice == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif choice == 3:
            centralLibrary.returnBook(student.returnBook())
        elif choice == 4:
            print("Thank you for visiting the library.")
            break
        else:
            print("Invalid choice!")
