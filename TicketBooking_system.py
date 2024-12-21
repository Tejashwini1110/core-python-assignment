def book_seat(total_seats, booked_seats, seat_number):
#Function to book a seat.
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    elif seat_number > total_seats or seat_number < 1:
        print(f"Invalid seat number {seat_number}. Please choose a valid seat.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} has been booked successfully.")
def cancel_seat(booked_seats, seat_number):
#Function to cancel a booking.
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} has been canceled.")
    else:
        print(f"Seat {seat_number} was not booked.")
def available_seats(total_seats, booked_seats):
#Function to get the list of available seats.
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
# Input Example
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_number = 3
cancel_seat_number = 5
# Booking a seat
book_seat(total_seats, booked_seats, book_seat_number)
# Canceling a seat
cancel_seat(booked_seats, cancel_seat_number)
# Display available seats
available = available_seats(total_seats, booked_seats)
print("Available seats:", available)
