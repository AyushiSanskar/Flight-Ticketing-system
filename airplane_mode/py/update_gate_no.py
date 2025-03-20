import frappe

def update_gate_number_in_tickets(doc, method):
    
     # Fetch all Airplane Tickets linked to the current Airplane Flight
  tickets = frappe.get_all('Airplane Ticket', filters={'flight': doc.name}, fields=['name', 'gate_number'])

# Iterate over each ticket and update the gate number
  # for ticket in tickets:
  #   ticket_doc = frappe.get_doc('Airplane Ticket', ticket['name'])
  #   ticket_doc.gate_no = doc.gate_number
  #   ticket_doc.save()