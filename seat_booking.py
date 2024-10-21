import sys
import os

# File to store seat reservation data
SEAT_FILE = 'seat_reservations.txt'

class SeatReservationSystem:
    def __init__(self, seat_file=SEAT_FILE):
        self.rows = 20
        self.seat_layout = "xx_xxxx_xx"
        self.seat_file = seat_file
        self.seats = self.load_seat_file()

    def load_seat_file(self):
        # Load the seat reservations from file, initialize if file doesn't exist
        if not os.path.exists(self.seat_file):
            seats = [["_" if c == "_" else "_" for c in self.seat_layout] for _ in range(self.rows)]
            self.save_seat_file(seats)
        else:
            with open(self.seat_file, 'r') as f:
                seats = [list(line.strip()) for line in f.readlines()]
        return seats

    def save_seat_file(self, seats):
        # Save the seat reservations back to the file
        with open(self.seat_file, 'w') as f:
            for row in seats:
                f.write("".join(row) + '\n')

    def seat_to_index(self, seat_id):
        # Convert a seat identifier like A1 to row, seat indices
        row = ord(seat_id[0].upper()) - ord('A')
        seat = int(seat_id[1:])
        return row, seat

    def is_seat_available(self, row, seat, num_seats):
        # Check if the seats in the range are available and ensure gaps cannot be booked
        for i in range(seat, seat + num_seats):
            if i >= len(self.seat_layout) or self.seats[row][i] != "_" or self.seat_layout[i] == "_":
                return False
        return True

    def book_seat(self, start_seat, num_seats):
        try:
            row, seat = self.seat_to_index(start_seat)
            if self.is_seat_available(row, seat, num_seats):
                for i in range(seat, seat + num_seats):
                    self.seats[row][i] = "X"  # Mark as reserved
                self.save_seat_file(self.seats)
                return "SUCCESS"
            else:
                # Check if the seat(s) is already booked
                if any(self.seats[row][i] == "X" for i in range(seat, seat + num_seats)):
                    return "FAIL - Seat(s) already booked"
                return "FAIL - Invalid seat or layout"
        except (IndexError, ValueError):
            return "FAIL"

    def cancel_seat(self, start_seat, num_seats):
        try:
            row, seat = self.seat_to_index(start_seat)
            for i in range(seat, seat + num_seats):
                if self.seats[row][i] == "X":
                    self.seats[row][i] = "_"  # Mark as available
                else:
                    return "FAIL"  # Seat wasn't reserved
            self.save_seat_file(self.seats)
            return "SUCCESS"
        except (IndexError, ValueError):
            return "FAIL"

def main():
    if len(sys.argv) != 4:
        print("FAIL")
        return

    action, start_seat, num_seats = sys.argv[1], sys.argv[2], int(sys.argv[3])
    system = SeatReservationSystem()

    if action == "BOOK":
        result = system.book_seat(start_seat, num_seats)
    elif action == "CANCEL":
        result = system.cancel_seat(start_seat, num_seats)
    else:
        result = "FAIL"

    print(result)

if __name__ == "__main__":
    main()