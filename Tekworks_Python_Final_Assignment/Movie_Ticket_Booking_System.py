def book_seat_function(booked_seats, seat):
    if seat in booked_seats:
        return "Seat " + str(seat) + " is already booked."
    booked_seats.append(seat)
    return "Seat " + str(seat) + " booked successfully."


def cancel_seat(booked_seats, seat):
    if seat not in booked_seats:
        return "Seat " + str(seat) + " is not booked."
    booked_seats.remove(seat)
    return "Seat " + str(seat) + " cancelled successfully."


def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]


total_seats = 10
booked_seats = [2, 5, 7]
book_seat_request = 3
cancel_seat_request = 5
booking_response = book_seat_function(booked_seats, book_seat_request)
print(booking_response)
cancellation_response = cancel_seat(booked_seats, cancel_seat_request)
print(cancellation_response)
available = available_seats(total_seats, booked_seats)
print("Available seats: " + str(available))
