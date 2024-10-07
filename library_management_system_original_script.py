
# This is the original basic script

books = {"book1": 3, "book2": 2, "book3": 0}
book_names = {"book1": "1984", "book2": "To Kill a Mockingbird", "book3": "The Great Gatsby"}

def add(b):
    if b in books:
        books[b] += 1
    else:
        books[b] = 1
    print(f"Book added: {b}")

def borrow(b):
    if books[b] > 0:
        books[b] -= 1
        print(f"You have borrowed {b}")
    else:
        print("Book not available.")

def main():
    while True:
        action = input("Enter 'A' to add a book or 'B' to borrow a book: ")
        if action == "A":
            book_id = input("Enter the book ID to add: ")
            add(book_id)
        elif action == "B":
            book_id = input("Enter the book ID to borrow: ")
            borrow(book_id)
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()