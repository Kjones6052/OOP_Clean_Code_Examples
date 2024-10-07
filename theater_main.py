
# Import class
from theater import Theater

# Write main script for the theater seats
def main():
    movie_theater = Theater(10,15) # 10 rows, 15 seats per row
    while True:
        try:
            movie_theater.display_seating_chart()
            row = int(input("Select row number: "))
            seat = int(input("Select seat number: "))
            if not movie_theater.reserve_seat(row, seat):
                print("Sorry, that seat is already reserved.")
            else:
                print(f"Seat reserved successfully at Row {row}, Seat {seat}.")
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
