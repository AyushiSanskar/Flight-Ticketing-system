# Copyright (c) 2025, Ayushi Dhamecha and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate_add_ons()
        self.calculate_total_amount()
        self.check_seat_availability()
        
        
    def check_seat_availability(self):
        if not self.flight:
            frappe.throw("Flight must be specified.")

        # Fetch the flight document
        flight = frappe.get_doc("Airplane Flight", self.flight)

        if not flight.airplane:
            frappe.throw("The selected flight does not have an associated airplane.")

        # Fetch the airplane document
        airplane = frappe.get_doc("Airplane", flight.airplane)

        if not airplane.capacity:
            frappe.throw("The associated airplane does not have a defined capacity.")

        # Retrieve the seating capacity
        capacity = airplane.capacity

        # Count existing tickets for the same flight
        existing_tickets_count = frappe.db.count(
            "Airplane Ticket",
            filters={
                "flight": self.flight,
                "docstatus": ["!=", 2]  # Exclude cancelled tickets
            }
        )

        # Check if adding a new ticket would exceed capacity
        if existing_tickets_count >= capacity:
            frappe.throw("No seats available for this flight.")

            
    def remove_duplicate_add_ons(self):
        """Ensure each add-on item is unique in the add_ons child table."""
        unique_items = set()
        to_remove = []
        for add_on in self.add_ons:
            if add_on.item in unique_items:
                to_remove.append(add_on)
            else:
                unique_items.add(add_on.item)

        for add_on in to_remove:
            self.remove(add_on)

        if to_remove:
            frappe.msgprint("Duplicate add-on items have been removed")

    def calculate_total_amount(self):
        """Calculate the total amount as Flight Price plus the sum of all add-on amounts."""
        add_ons_total = sum(add_on.amount for add_on in self.add_ons)
        self.total_amount = self.flight_price + add_ons_total
        
    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Cannot submit Airplane Ticket unless status is 'Boarded'.")

