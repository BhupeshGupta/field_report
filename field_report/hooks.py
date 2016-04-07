app_name = "field_report"
app_title = "Field Report"
app_publisher = "Arun Logistics"
app_description = "Management Of Mobile Reporting Clients"
app_icon = "icon-mobile-phone"
app_color = "rgb(123, 107, 107)"
app_email = "info@arungas.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/field_report/css/field_report.css"
# app_include_js = "/assets/field_report/js/field_report.js"

# include js, css files in header of web template
# web_include_css = "/assets/field_report/css/field_report.css"
# web_include_js = "/assets/field_report/js/field_report.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "field_report.install.before_install"
# after_install = "field_report.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "field_report.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"field_report.tasks.all"
# 	],
# 	"daily": [
# 		"field_report.tasks.daily"
# 	],
# 	"hourly": [
# 		"field_report.tasks.hourly"
# 	],
# 	"weekly": [
# 		"field_report.tasks.weekly"
# 	]
# 	"monthly": [
# 		"field_report.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "field_report.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "field_report.event.get_events"
# }

boot_session = "field_report.field_report.startup_boot_info.cached_boot_info"
extend_bootinfo = "field_report.field_report.startup_boot_info.non_cached_boot_info"
on_session_creation = "field_report.field_report.startup_boot_info.on_session_creation"