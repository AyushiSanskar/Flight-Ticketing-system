import frappe
import random
import string


def assign_seat(doc, method):
    seat_letters = 'ABCDEF'  # Seat columns
    seats_per_row = len(seat_letters)
    max_rows = 30  # Total number of rows

    # Fetch existing tickets for the flight
    existing_tickets = frappe.get_all(
        'Airplane Ticket',
        filters={'flight': doc.flight},
        fields=['seat'],
        order_by='creation'
    )

    # Determine the next available seat
    total_booked = len(existing_tickets)
    if total_booked >= max_rows * seats_per_row:
        frappe.throw("All seats are booked for this flight.")

    row_number = (total_booked // seats_per_row) + 1
    seat_letter = seat_letters[total_booked % seats_per_row]
    doc.seat = f"{row_number}{seat_letter}"
    
    # # Generate a random integer between 1 and 100
    # random_number = random.randint(1, 30)
    # # Choose a random letter between A and E
    # random_letter = random.choice('ABCDE')
    # # Combine to form the seat identifier
    # doc.seat = f"{random_number}{random_letter}"