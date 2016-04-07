# Copyright (c) 2013, Arun Logistics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.sessions import clear_cache

class UserConfig(Document):
	def validate(self):
		clear_cache(self.user)