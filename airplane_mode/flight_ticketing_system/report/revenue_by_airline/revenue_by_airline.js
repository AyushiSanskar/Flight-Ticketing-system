// Copyright (c) 2025, Ayushi Dhamecha and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue By Airline"] = {
	"filters": [
		{
			"fieldname": "airline",
			"label": __("Airline"),
			"fieldtype": "Link",
			"options": "Airline"
		},
		{
			"fieldname": "currency",
			"label": __("Revenue"),
			"fieldtype": "Currency",
		},
	]
};
