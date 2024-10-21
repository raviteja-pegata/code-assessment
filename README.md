# code-assessment

Seat Reservation System Documentation
This Python script is designed to manage seat reservations for an airline company. The airplane has a fixed seat layout with 20 rows, and each row follows the structure xx_xxxx_xx, which represents available seats with gaps that cannot be booked. The system is controlled entirely via command-line inputs, allowing users to book or cancel seat reservations, with the seat reservation state being persisted in a file (seat_reservations.txt).

Structure and Functionality
1. SeatReservationSystem Class
This is the core class of the system, which manages all the logic related to seat booking, cancellation, and file handling.

a) __init__(self, seat_file)
Purpose: Initializes the system with the seat layout and loads the current state of reservations from the seat_reservations.txt file.

Attributes:
    self.rows: Set to 20, representing the number of rows in the airplane.
    self.seat_layout: A string representation of the seat layout xx_xxxx_xx, where _ denotes gaps.
    self.seat_file: The file name for saving the seat reservation state (seat_reservations.txt).
    self.seats: A 2D list representing the current state of seat reservations, loaded from the file.

b) load_seat_file(self)
Purpose: Loads the seat reservation status from a file. If the file doesn't exist, it creates a new one with the initial layout (all seats available).

Behavior:
Reads the file line by line and converts each row into a list of characters representing seat states (_ for available and X for booked).
Initializes a new seat layout if the file doesn’t exist.

c) save_seat_file(self, seats)
Purpose: Saves the current seat reservation status to the seat_reservations.txt file.

Behavior:
Writes each row of seat states (as a string) to the file, ensuring persistence of the current seat layout.

d) seat_to_index(self, seat_id)
Purpose: Converts a seat identifier (e.g., A1) into corresponding row and seat indices that can be used in the list representation.

Behavior:
Converts the row letter (A to T) into a numeric index.
Converts the seat number into an index for the seat in the row.

e) is_seat_available(self, row, seat, num_seats)
Purpose: Checks whether the requested seats are available and not over any gaps.

Behavior:
Iterates over the requested range of seats, verifying that each seat is available (_) and that no gaps (_ in the layout) are included in the range.

f) book_seat(self, start_seat, num_seats)
Purpose: Books the requested number of seats starting from the given seat.

Behavior:
    Converts the seat identifier to row and seat indices.
    Uses is_seat_available to check if the seats are free.
    If all seats are available, marks them as booked (X).
    If any seat is already booked, returns a failure message ("Seat(s) already booked").
    If invalid seat layout or gap crossing is detected, returns a failure message ("Invalid seat or layout").

g) cancel_seat(self, start_seat, num_seats)
Purpose: Cancels the booking for the given seat range, making them available again.
Behavior:
    Converts the seat identifier to row and seat indices.
    Checks if the seat is booked (X). If so, marks it as available (_).
    If any seat in the range was not booked, returns a failure message ("Seat wasn't reserved").
    2. main() Function
    This is the main entry point for the script. It processes command-line arguments to perform seat booking or cancellation.

a) Command-line Interface:
The system accepts exactly 4 arguments:

Action: Either BOOK or CANCEL.
    Start Seat: The starting seat identifier (e.g., A1).
    Number of Seats: The number of consecutive seats to book or cancel.

b) Behavior:
Based on the action (BOOK or CANCEL), the respective function (book_seat or cancel_seat) is called.
Outputs SUCCESS or FAIL based on the operation result.

 Error Handling:
    If an invalid number of arguments is provided, the script prints "FAIL".
    Errors related to seat booking or cancellation (e.g., already booked, invalid seat, gaps in the layout) are handled and reported via specific messages (e.g., "FAIL - Seat(s) already booked" or "FAIL - Invalid seat or layout").
    Error Handling
    The system is built with robust error handling to ensure that invalid operations do not crash the program and that the user is informed of the exact reason for failure.

    Invalid Number of Arguments:

    If the script is not provided exactly 4 arguments, it immediately prints "FAIL" and exits. This ensures the correct usage of the system.
    Invalid Seat Identifiers:

    The function seat_to_index converts seat identifiers (like A1) to row and seat indices. If an invalid seat is provided (e.g., a seat outside the range), the system catches IndexError or ValueError and returns "FAIL". This ensures no invalid seat numbers cause unexpected crashes.
    Double Booking:

    If the user tries to book a seat that is already reserved, the book_seat function detects this and returns "FAIL - Seat(s) already booked". This prevents multiple bookings of the same seat.
    Booking Over Gaps:

    If the user tries to book seats across gaps (represented by _), the system prevents the operation by returning "FAIL - Invalid seat or layout". This ensures that the booking remains consistent with the seat layout.
    Cancelling Unbooked Seats:

    The cancel_seat function checks whether the seat is already booked. If the seat wasn't booked, it returns "FAIL - Seat wasn't reserved", preventing the user from canceling an unbooked seat.
    Seat Layout Integrity:

    The system ensures that any booking or cancellation that crosses gaps in the layout is prevented. This prevents invalid bookings from breaking the seat layout structure.



Example usage

# Book 2 seats starting from A1
python3 seat_booking.py BOOK A1 2
# Output: SUCCESS

# Attempt to book the same seats again
python3 seat_booking.py BOOK A1 2
# Output: FAIL - Seat(s) already booked

# Cancel the booking for 2 seats starting from A1
python3 seat_booking.py CANCEL A1 2
# Output: SUCCESS

# Attempt to book seats that cross a gap
python3 seat_booking.py BOOK A1 5
# Output: FAIL - Invalid seat or layout
