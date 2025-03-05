# Copyright (c) 2025, Ayushi Dhamecha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate_add_ons()
        self.calculate_total_amount()

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
