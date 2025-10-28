// Copyright (c) 2024, Md Omar Faruk and contributors
// For license information, please see license.txt

frappe.ui.form.on("Device Configuration", {
	refresh(frm) {
		frm.add_custom_button(__("Fetch Check-in"), function () {
			// Create a new dialog
			let d = new frappe.ui.Dialog({
				title: __("Fetch Attendance"),
				fields: [
					{
						fieldname: "start_date",
						label: __("Start Date"),
						fieldtype: "Datetime",
						reqd: 1,
					},
					{
						fieldname: "end_date",
						label: __("End Date"),
						fieldtype: "Datetime",
						reqd: 1,
					},
				],
				primary_action_label: __("Fetch"),
				primary_action(values) {
					// Call server-side method to fetch attendance
					frappe.call({
						method: "attendance_sync.attendance_sync.doctype.device_configuration.device_configuration.fetch_attendance",
						args: {
							start_date: values.start_date,
							end_date: values.end_date,
							device_ip: frm.doc.device_ip,
							major: frm.doc.major,
							minor: frm.doc.minor,
							device_user: frm.doc.device_user,
							device_user_password: frm.doc.device_user_password,
						},
						callback: function (r) {
							if (r.message) {
								frappe.msgprint(__("Attendance data fetched successfully."));
								// You can handle the fetched data here
							} else {
								frappe.msgprint(__("Failed to fetch attendance data."));
							}
						},
					});
					d.hide(); // Close the dialog after submit
				},
			});
			d.show();
		}).addClass("btn-primary");
	},
});
