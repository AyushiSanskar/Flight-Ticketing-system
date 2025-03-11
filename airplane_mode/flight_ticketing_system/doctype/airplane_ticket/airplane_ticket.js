// Copyright (c) 2025, Ayushi Dhamecha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    // ----------------------This is show the error massage----------------------------------
	// validate: function(frm) {
    //     let items = frm.doc.add_ons.map(add_on => add_on.item);
    //     let unique_items = new Set(items);
    //     if (items.length !== unique_items.size) {
    //         frappe.msgprint(__('Duplicate add-on items are not allowed.'));
    //         frappe.validated = false;
    //     }
    // }

    // ------------------------------------ Seat assign using custom button--------------------------------
    refresh: function(frm) {
        frm.add_custom_button(__('assign seat'), function() {
          
            let d = new frappe.ui.Dialog({
                title: 'Select Seat',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data'
                    }
                ],
                size: 'small', // small, large, extra-large 
                primary_action_label: 'Submit',
                primary_action(values) {
                    if (values.seat_number) {
                        frm.set_value('seat', values.seat_number);
                        frm.save();
                        dialog.hide();
                    } else {
                        frappe.msgprint(__('Please enter a value.'));
                    }
                    console.log(values);
                    frappe.msgprint("seat assigned");
                    d.hide();
                }
            });
            
            d.show();
        }, __("Action"));
    }
});
