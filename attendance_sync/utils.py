from datetime import datetime

import frappe

from attendance_sync.attendance_sync.Attendance import Attendance


def get_attendance_from_device():
	# Fetch all Device Configuration documents
	device_configurations = frappe.get_all(
		"Device Configuration", fields=["device_ip", "major", "minor", "device_user", "device_user_password"]
	)

	# Get the current time
	now = datetime.now()
	start_time = now.replace(hour=0, minute=0, second=0, microsecond=0)
	end_time = now.replace(hour=23, minute=59, second=59, microsecond=0)

	# Loop through each device configuration
	for device in device_configurations:
		# Create an instance of the Attendance class for each device
		attendance = Attendance(
			device_ip=device.device_ip,
			major=device.major,
			minor=device.minor,
			device_user=device.device_user,
			device_password=device.device_user_password,
		)
		# Process the attendance for the given device
		attendance.get_and_process_attendance(start_time, end_time)
