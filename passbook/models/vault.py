from passbook.features.orm import db
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from .base import BaseTable

class Vault(BaseTable):
	src = db.Column(db.String(255))
	secret_key = db.Column(db.Unicode(255))
	token = db.Column(EncryptedType(db.Unicode, secret_key, AesEngine, 'pkcs5'))

	def __init__(self, token=None, src='http://127.0.0.1:5000/'):
		self.src = src
		self.token = token
		#self.cert = cert
		#self.access_key
		#self.secret_key
		#self.expiration_time

	@staticmethod
	def create(filename, password):
		pass

	def write_to_file(self, filename, password):
		pass

class VaultCache(object):
	def __init__(self, size):
		self.size = size

class BackupVault(object):
	pass