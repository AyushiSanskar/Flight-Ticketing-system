// Copyright (c) 2025, Ayushi Dhamecha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
    onload: function(frm) {
        frm.set_query('shop_type', function() {
            return {
                filters: {
                    'enabled': 1
                }
            };
        });
    }
});
