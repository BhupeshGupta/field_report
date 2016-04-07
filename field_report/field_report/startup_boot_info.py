import frappe
import json
from frappe.utils import nowtime

from frappe.exceptions import DoesNotExistError
from frappe.utils import now_datetime

def cached_boot_info(bootinfo):
	global_config = json.loads(frappe.get_doc("Field App Config", '').json_config)

	bootinfo.field_app = frappe._dict({
		'config': global_config,
		'time': nowtime()
	})

	user_config = frappe.db.get_values("User Config", {'user': bootinfo.user.name}, fieldname='json_config')
	if user_config:
		bootinfo.field_app.config.update(json.loads(user_config[0][0]))

def non_cached_boot_info(bootinfo):
	app = frappe.get_request_header('App-Version')
	if app:
		device = json.loads(frappe.get_request_header('User-Id'))
		device_obj = frappe.get_doc("Field App Device", device['serial'])
		bootinfo.field_app.config.update(json.loads(device_obj.json_config))

def on_session_creation(login_manager):
	app = frappe.get_request_header('App-Version')
	if app:
		device = json.loads(frappe.get_request_header('User-Id'))

		device = {
			'serial': device['serial'],
			'platform': device['platform'],
			'platform_version': device['version'],
			'uuid': device['uuid'],
			'last_active_on': now_datetime(),
			'user': login_manager.user,
			'doctype': 'Field App Device',
			'last_active_user': login_manager.user,
			'app_version': frappe.get_doc("Field App Version", app).name,
			'device_meta': frappe.get_request_header('User-Id')
		}

		device_obj = None
		try:
			device_obj = frappe.get_doc("Field App Device", device['serial'])
			device_obj.update(device)
		except DoesNotExistError:
			device_obj = frappe.get_doc(device)

		device_obj.ignore_permissions = True
		device_obj.save()
