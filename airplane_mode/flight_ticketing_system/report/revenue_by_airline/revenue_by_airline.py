# # Copyright (c) 2025, Ayushi Dhamecha and contributors
# # For license information, please see license.txt

# import frappe
# from frappe import _, msgprint

# def execute(filters=None):
    
# 	columns = get_columns()
#     data, total_revenue = get_data()
#     # chart = get_chart_data(data)
#     # report_summary = get_report_summary(total_revenue)
#     return columns, data

# def get_columns():
#     return [
#         {
#             "label": _("Airline"),
#             "fieldname": "airline",
#             "fieldtype": "Link",
#             "options": "Airline",
#             "width": 200
#         },
#         {
#             "label": _("Revenue"),
#             "fieldname": "revenue",
#             "fieldtype": "Currency",
#             "width": 150
#         }
#     ]
    
# def get_data():
#     # Fetch all airlines
#     airlines = frappe.get_all('Airline', fields=['name1'])

#     data = []
#     total_revenue = 0.0

#     for airline in airlines:
#         # Calculate revenue for each airline
#         revenue = frappe.db.get_value('Airline Ticket',
#             # filters={'airline': airline.name, 'docstatus': 1},
#             fieldname='total_amount') or 0.0

#         data.append({
#             'airline': airline.name,
#             'revenue': revenue
#         })

#         total_revenue += revenue

#     # Sort data by revenue in descending order
#     data.sort(key=lambda x: x['revenue'], reverse=True)

#     return data, total_revenue


# Copyright (c) 2025, Ayushi Dhamecha and contributors
# For license information, please see license.txt

# import frappe
# from frappe import _, msgprint

# def execute(filters=None):
#     columns = get_columns()
#     data, total_revenue = get_data()
#     # If you intend to include chart and summary data, uncomment the following lines:
#     # chart = get_chart_data(data)
#     # report_summary = get_report_summary(total_revenue)
#     # return columns, data, None, chart, report_summary
#     return columns, data

# def get_columns():
#     return [
#         {
#             "label": _("Airline"),
#             "fieldname": "airline",
#             "fieldtype": "Link",
#             "options": "Airline",
#             "width": 200
#         },
#         {
#             "label": _("Revenue"),
#             "fieldname": "revenue",
#             "fieldtype": "Currency",
#             "width": 150
#         }
#     ]

# def get_data():
#     # Fetch all airlines
#     airlines = frappe.get_all('Airline', fields=['name1'])

#     data = []
#     total_revenue = 0.0

#     for airline in airlines:
#         # Calculate revenue for each airline
#         revenue = frappe.db.get_value(
#             'Airplane Ticket',
#             # filters={'airline': airline.name, 'docstatus': 1},
#             fieldname='total_amount'
#         )
#     	revenue = float(revenue) if revenue is not None else 0.0
     
#         data.append({
#             'airline': airline.name,
#             'revenue': revenue
#         })

#         total_revenue += revenue

#     # Sort data by revenue in descending order
#     data.sort(key=lambda x: x['revenue'], reverse=True)

#     return data, total_revenue


# import frappe
# from frappe import _, msgprint

# def execute(filters=None):
#     columns = get_columns()
#     data, total_revenue = get_data()
#     # If you intend to include chart and summary data, uncomment the following lines:
#     # chart = get_chart_data(data)
#     # report_summary = get_report_summary(total_revenue)
#     # return columns, data, None, chart, report_summary
#     return columns, data

# def get_columns():
#     return [
#         {
#             "label": _("Airline"),
#             "fieldname": "airline",
#             "fieldtype": "Link",
#             "options": "Airline",
#             "width": 200
#         },
#         {
#             "label": _("Revenue"),
#             "fieldname": "revenue",
#             "fieldtype": "Currency",
#             "width": 150
#         }
#     ]

# def get_data():
#     # Fetch all airlines
#     airlines = frappe.get_all('Airline', fields=['name1'])

#     data = []
#     total_revenue = 0.0

#     for airline in airlines:
#         # Calculate revenue for each airline
#         revenue = frappe.db.get_value(
#             'Airplane Ticket',
#             # filters={'airline': airline.name, 'docstatus': 1},
#             fieldname='total_amount'
#         )
#         revenue = float(revenue) if revenue is not None else 0.0

#         data.append({
#             'airline': airline.name1,
#             'revenue': revenue
#         })

#         total_revenue += revenue

#     # Sort data by revenue in descending order
#     data.sort(key=lambda x: x['revenue'], reverse=True)

#     return data, total_revenue


# import frappe
# from frappe import _

# def execute(filters=None):
#     columns = get_columns()
#     data, total_revenue = get_data(filters)
#     chart = get_chart_data(data)
#     report_summary = get_report_summary(total_revenue)
#     return columns, data, None, chart, report_summary

# def get_columns():
#     return [
#         {
#             "label": _("Airline"),
#             "fieldname": "airline",
#             "fieldtype": "Link",
#             "options": "Airline",
#             "width": 200
#         },
#         {
#             "label": _("Revenue"),
#             "fieldname": "revenue",
#             "fieldtype": "Currency",
#             "width": 150
#         }
#     ]

# def get_data(filters):
#     # SQL query to fetch revenue by airline
#     query = """
#         SELECT
#             airline,
#             SUM(total_amount) AS total_revenue
#         FROM
#             `tabAirplane Ticket`
#         GROUP BY
#             airline
#         ORDER BY
#             total_revenue DESC
#     """

#     data = frappe.db.sql(query, as_dict=True)

#     # Calculate total revenue
#     total_revenue = sum(d['revenue'] for d in data)

#     return data, total_revenue

# def get_chart_data(data):
#     labels = [d['airline'] for d in data]
#     values = [d['revenue'] for d in data]

#     return {
#         'data': {
#             'labels': labels,
#             'datasets': [{'values': values}]
#         },
#         'type': 'donut',
#         'height': 300
#     }

# def get_report_summary(total_revenue):
#     return [{
#         'value': total_revenue,
#         'label': _('Total Revenue'),
#         'datatype': 'Currency',
#         'currency': frappe.defaults.get_global_default('currency')
#     }]


import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data()

    # Calculate total revenue
    total_revenue = sum(d["revenue"] for d in data)

    report_summary = [
        {"label": _("Total Revenue"), "value": total_revenue, "indicator": "Green"}
    ]

    # Chart Configuration
    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [{"values": [d["revenue"] for d in data]}],
        },
        "type": "donut",
    }

    return columns, data, None, chart, report_summary

def get_columns():
    """Define report columns."""
    return [
        {"label": _("Airline"), "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"label": _("Revenue"), "fieldname": "revenue", "fieldtype": "Currency", "width": 150},
    ]

def get_data():
    """Fetch revenue data grouped by airline."""
    airlines = frappe.get_all("Airline", fields=["name"])
    data = []

    for airline in airlines:
        revenue = frappe.db.sql("""
            SELECT SUM(at.total_amount) 
            FROM `tabAirplane Ticket` at
            JOIN `tabAirplane Flight` af ON at.flight = af.name
            JOIN `tabAirplane` a ON af.airplane = a.name
            WHERE a.airline = %s
        """, (airline.name,), as_list=True)[0][0] or 0

        data.append({"airline": airline.name, "revenue": revenue})

    return data