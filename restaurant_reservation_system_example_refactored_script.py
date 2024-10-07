
# Refactored Restaurant Reservation Script
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = {1: None, 2: None, 3: None} # Table number: Reservation name

    def reserve_table(self, customer_name, table_number):
        if self.tables[table_number] is True:
            self.tables[table_number] = customer_name
            print(f"Table {table_number} reserved for {customer_name}.")
        else:
            print(f"Sorry, table {table_number} is already reserved.")

    def cancel_reservation(self, table_number):
        if self.tables[table_number] is not None:
            reserved_name = self.tables[table_number]
            self.tables[table_number] = None
            print(f"Reservation for {reserved_name} at table {table_number} canceled.")
        else:
            print("There is no reservation for this table.")

def main():
    my_restaurant = Restaurant("Gourmet Python")
    while True:
        try:
            choice = input("Do you want to reserve or cancel a table? (reserve/cancel):").lower()
            if choice not in ["reserve", "cancel"]:
                raise ValueError("Invalid choice. Please  choose 'reserve' or 'cancel'.")
            table = int(input("Enter table number (1-3): "))
            if choice == "reserve":
                name = input("Enter the name for reservation: ")
                my_restaurant.reserve_table(name, table)
            elif choice == "cancel":
                my_restaurant.cancel_reservation(table)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()