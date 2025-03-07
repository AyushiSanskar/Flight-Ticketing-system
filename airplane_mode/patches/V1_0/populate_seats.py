# import frappe

# def execute():
#     seat_letters = 'ABCDEF'  # Seat columns
#     seats_per_row = len(seat_letters)
#     max_rows = 30  # Total number of rows
#     max_seats = max_rows * seats_per_row

#     # Fetch all flights
#     flights = frappe.get_all('Airplane Ticket', fields=['name'])

#     for flight in flights:
#         tickets = frappe.get_doc(
#             'Airplane Ticket',
#             flight.name,
#         )
#         if not tickets.seat:
#             frappe.db.set_value('Airplane Ticket', ticket.name, 'seat', seat_number)
#         total_booked = len(tickets)
#     frappe.db.commit()


import frappe

def execute():
    """Patch to populate seat field in existing Airplane Ticket documents."""
    
    # Fetch all existing tickets that do not have a seat assigned
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["is", "not set"]}, fields=["name", "flight"])

    if not tickets:
        frappe.logger().info("No tickets need seat assignment.")
        return

    for ticket in tickets:
        flight = ticket["flight"]

        # Get already booked seats for this flight
        booked_seats = frappe.get_all(
            "Airplane Ticket",
            filters={"flight": flight},
            fields=["seat"]
        )

        # Convert to a set for fast lookup
        taken_seats = {t["seat"] for t in booked_seats if t["seat"]}

        # Generate seat numbers row-wise (1A, 1B, 1C, ..., 30F)
        all_seats = [f"{row}{col}" for row in range(1, 31) for col in "ABCDEF"]

        # Find the first available seat
        available_seat = next((seat for seat in all_seats if seat not in taken_seats), None)

        if available_seat:
            frappe.db.set_value("Airplane Ticket", ticket["name"], "seat", available_seat)
        else:
            frappe.logger().warning(f"No available seats for flight {flight}")

    frappe.db.commit()
    frappe.logger().info("Seat assignment patch executed successfully.")
