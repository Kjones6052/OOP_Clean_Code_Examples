
# Inherited Restaurant Reservation Script

reservations = {"tabel1": "", "table2": "", "table3": ""}
tables = [1, 2, 3]

def check_table(table_number):
    if reservations(f"table{table_number}"):
        return True
    return False

def book_table():
    table_number = int(input("Enter table number (1-3): "))
    if table_number not in tables:
        print("Invalid table number.")
        return
    if check_table(table_number):
        print(f"Sorry, table {table_number} is already booked.")
    else:
        name = input("Enter your name for the reservation: ")
        reservations[f"table{table_number}"] = name
        print(f"Table {table_number} boofed for {name}.")

def cancel_booking():
    table_number = int(input("Enter table number (1-3): "))
    if table_number not in tables:
        print("Invalid table number.")
        return
    if not check_table(table_number):
        print(f"No reservation for table {table_number}.")
    else:
        reservations[f"table{table_number}"] = ""
        print(f"Reservation for table {table_number} canceled.")

def main():
    while True:
        choice = input("Do you want to book or cancel a table? (book/cancel):").lower()
        if choice == "book":
            book_table()
        elif choice == "cancel":
            cancel_booking()
        else: 
            print("Invalid choice. Please type 'book' or 'cancel'.")

if __name__ == "__main__":
    main()