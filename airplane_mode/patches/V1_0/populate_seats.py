import frappe

def execute():
    seat_letters = 'ABCDEF'  # Seat columns
    seats_per_row = len(seat_letters)
    max_rows = 30  # Total number of rows
    max_seats = max_rows * seats_per_row

    # Fetch all flights
    flights = frappe.get_all('Airplane Ticket', fields=['name'])

    for flight in flights:
        tickets = frappe.get_doc(
            'Airplane Ticket',
            flight.name,
        )
        if not tickets.seat:
            frappe.db.set_value('Airplane Ticket', ticket.name, 'seat', seat_number)
        total_booked = len(tickets)
    frappe.db.commit()