from passbook.features.extensions import db
from . import TimestampMixin

class Vault(object):
	def __init__(self, password, filename):
		self.password = password
		self.filename = filename
		self.records = []

	@staticmethod
	def create(filename, password):
		pass

	def write_to_file(self, filename, password):
		pass

class VaultCache(object):
	def __init__(self, size):
		self.size = size