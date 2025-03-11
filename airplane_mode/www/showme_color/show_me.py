import frappe

def get_context(context):
    # Retrieve the 'color' query parameter; default to 'black' if not provided
    color = frappe.local.form_dict.get('color', 'black')
    context.color = color
   