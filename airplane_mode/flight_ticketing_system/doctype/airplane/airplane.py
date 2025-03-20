# Copyright (c) 2025, Ayushi Dhamecha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.naming import make_autoname
from frappe.model.document import Document


class Airplane(Document):
	
	
	def autoname(doc):
		if doc.airline:
			doc.name = make_autoname(f"{doc.airline}-.###")
		else:
			doc.name = make_autoname("AIRPLANE-.###") 
