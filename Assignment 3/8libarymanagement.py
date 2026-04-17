
import csv

class Book:
    """
    class to represent a book
    """

    def __init__(self, book_id, title, author, status="available"):
        """
        initialize book attributes
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        
    def to_list(self):
        """
        convert book object to list for file storage
        """
        return [self.book_id, self.title, self.author, self.status]


class Library:
    """
    class to manage library operations
    """
    def __init__(self, file_name):
        """
        initialize library with file name
        """
        self.file_name = file_name
    def load_books(self):
        """
        load books from file
        """
        books = []
        try:
            with open(self.file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    books.append(Book(row[0], row[1], row[2], row[3]))
        except FileNotFoundError:
            pass
        return books
    def save_books(self, books):
        """
        save books to file
        """
        try:
            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                for book in books:
                    writer.writerow(book.to_list())
        except Exception:
            print("error while saving books")

    def search_book(self, keyword):
        """
        search book by title
        """
        books = self.load_books()
        found = False
        for book in books:
            if keyword.lower() in book.title.lower():
                print(f"{book.book_id} | {book.title} | {book.author} | {book.status}")
                found = True
        if not found:
            print("no book found")

    def borrow_book(self, book_id):
        """
        borrow a book if available
        """
        books = self.load_books()
        for book in books:
            if book.book_id == book_id:
                if book.status == "available":
                    book.status = "borrowed"
                    self.save_books(books)
                    print("book borrowed successfully")
                    return
                else:
                    print("book already borrowed")
                    return
        print("book not found")

    def return_book(self, book_id):
        """
        return a borrowed book
        """
        books = self.load_books()
        for book in books:
            if book.book_id == book_id:
                if book.status == "borrowed":
                    book.status = "available"
                    self.save_books(books)
                    print("book returned successfully")
                    return
                else:
                    print("book was not borrowed")
                    return
        print("book not found")


# create library object
library = Library("books.csv")

# sample initial data if file is empty
try:
    open("books.csv", "x").close()
    library.save_books([
        Book("1", "python basics", "john doe"),
        Book("2", "data structures", "jane smith"),
        Book("3", "oop concepts", "alex ray")
    ])
except FileExistsError:
    pass


# main menu loop
while True:
    print("\n1 search book")
    print("2 borrow book")
    print("3 return book")
    print("4 exit")

    choice = input("enter choice: ")

    if choice == "1":
        keyword = input("enter book title to search: ")
        library.search_book(keyword)
    elif choice == "2":
        book_id = input("enter book id to borrow: ")
        library.borrow_book(book_id)
    elif choice == "3":
        book_id = input("enter book id to return: ")
        library.return_book(book_id)
    elif choice == "4":
        break
    else:
        print("invalid choice")