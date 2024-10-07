
# Refined Library Management System Script

class Library:
    def __init__(self):
        self.books = {"1984": 5, "To Kill a Mockingbord": 4} # Book Title: Quantity

    def add_book(self, title):
        if title in self.books:
            self.books[title] += 1
        else:
            self.books[title] = 1
        print(f"Added {title} to the library.")

    def borrow_book(self, title):
        if self.books.get(title, 0) > 0:
            self.books[title] -= 1
            print(f"You have borrowed {title}.")
        else:
            print(f"Sorry, {title} is not available.")

def main():
    my_library = Library()
    while True:
        try:
            action = input("Enter 'add' to add a book or 'borrow' to borrow a book: ").lower()
            if action not in ["add", "borrow"]:
                raise ValueError("Invalid action. Please choose 'add' or 'borrow'.")
            book_title = input("Enter the book title: ")
            if action == "add":
                my_library.add_book(book_title)
            elif action == "borrow":
                my_library.borrow_book(book_title)
            else:
                print("Invalid action")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()