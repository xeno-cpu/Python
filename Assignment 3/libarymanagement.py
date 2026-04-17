import json

class Library:
    def __init__(self, db_file="library.json"):
        self.db_file = db_file
        self.books = self.load_data()

    def load_data(self):
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author, isbn):
        """Adds a new book to the library."""
        self.books[isbn] = {
            "title": title,
            "author": author,
            "borrowed": False
        }
        self.save_data()
        print(f"Book '{title}' added successfully.")

    def borrow_book(self, isbn):
        if isbn in self.books:
            if not self.books[isbn]['borrowed']:
                self.books[isbn]['borrowed'] = True
                self.save_data()
                print(f"Success: You borrowed '{self.books[isbn]['title']}'.")
            else:
                print("Error: This book is already borrowed.")
        else:
            print("Error: ISBN not found.")

    def return_book(self, isbn):
        if isbn in self.books:
            self.books[isbn]['borrowed'] = False
            self.save_data()
            print(f"Success: '{self.books[isbn]['title']}' returned.")
        else:
            print("Error: ISBN not found.")

    def search_book(self, title):
        results = [b for b in self.books.values() if title.lower() in b['title'].lower()]
        return results

# Interactive Logic
if __name__ == "__main__":
    lib = Library()
    
    # Adding a sample book 
    if not lib.books:
        lib.add_book("The Great Gatsby", "F. Scott Fitzgerald", "12345")
        lib.add_book("1984", "George Orwell", "67890")

    print("--- Library System ---")
    print("1. Search | 2. Borrow | 3. Return | 4. Exit")
    
    while True:
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            t = input("Enter book title to search: ")
            print("Results:", lib.search_book(t))
        elif choice == "2":
            i = input("Enter ISBN to borrow: ")
            lib.borrow_book(i)
        elif choice == "3":
            i = input("Enter ISBN to return: ")
            lib.return_book(i)
        elif choice == "4":
            break
        