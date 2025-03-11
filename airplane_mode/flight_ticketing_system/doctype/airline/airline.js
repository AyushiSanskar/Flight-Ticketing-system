// Copyright (c) 2025, Ayushi Dhamecha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        // if (frm.doc.website) {
        //     frm.add_custom_button(__('Visit Website'), function() {
        //         window.open(frm.doc.website, '_blank');
        //     }).addClass('btn-primary');
        // }
        if (frm.doc.website) {
            frm.add_web_link(__(frm.doc.website), 'Visit Website');
        }
	},
    website: function(frm) {
        // Trigger refresh to update the 'View Website' link when the website field changes
        frm.trigger('refresh');
    }
});
