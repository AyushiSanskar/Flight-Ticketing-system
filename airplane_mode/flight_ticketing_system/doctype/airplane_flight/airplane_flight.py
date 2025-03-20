# Copyright (c) 2025, Ayushi Dhamecha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	
    def on_submit(self):
        self.status = "Completed"
        self.db_set("status", "Completed") 
        
    # def on_update(self):
    # # Check if the gate number has changed
    #     if self.has_value_changed('gate_number'):
    #         # Enqueue the background job to update tickets
    #         frappe.enqueue('airplane_mode.py.update_gate_no.update_gate_number_in_tickets', flight_id=self.name, new_gate_number=self.gate_number)
    
 