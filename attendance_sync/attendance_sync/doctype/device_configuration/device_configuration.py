# Copyright (c) 2024, Md Omar Faruk and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class DeviceConfiguration(Document):
	pass


@frappe.whitelist()
def fetch_attendance(start_date, end_date, device_ip, major, minor, device_user, device_user_password):
	# Queue the attendance fetching process
	frappe.enqueue(
		"attendance_sync.attendance_sync.Attendance.process_attendance_in_background",
		start_date=start_date,
		end_date=end_date,
		device_ip=device_ip,
		major=major,
		minor=minor,
		device_user=device_user,
		device_user_password=device_user_password,
		queue="long",
		timeout=3000,
	)
	frappe.msgprint(_("Attendance fetching has been queued."))
	return "Attendance fetch process has been queued."
