import base64
import string

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random as CryptoRandom

class CryptoHelper:
	def __init__(self, key, salt_length):
		self.key = key
		self.salted_key = None
		self.salt_length = salt_length

	def digest_key(self):
		key == self.salted_key if self.salted_key != None else self.key
		return SHA256.new(key).digest()

	def add_salt(self):
		ch = string.ascii_letters + string.punctuation + string.digits
		salt = "".join(choice(ch) for i in range(self.salt_length)).encode()
		self.salted_key = salt + self.key
		return salt

	def encrypt(self, secret):
		IV = CryptoRandom.new().read(AES.block_size)
		aes = AES.new(self.digest_key(), AES.MODE_CBC, IV)
		padding = AES.block_size - len(secret) % AES.block_size
		secret += bytes([padding]) * padding
		data = IV + aes.encrypt(secret)
		self.salted_key = None
		return base64.b64encode(data)

	def decrypt(self, encrypted_secret):
		encrypted_secret = base64.b64decode(encrypted_secret)
		IV = encrypted_secret[:AES.block_size]
		aes = AES.new(self.digest_key(), AES.MODE_CBC, IV)
		data = aes.decrypt(encrypted_secret[AES.block_size:])
		padding = data[-1]
		assert data[-padding:] == (bytes([padding]) * padding)
		self.salted_key = None
		return data[:-padding]

class RekeyHelper:
	def __init__(self, records):
		pass

	@staticmethod
	def get_new_key():
		pass

	@staticmethod
	def rekey_records(records):
		pass

	@staticmethod
	def rekey_db_key():
		pass

	@staticmethod
	def rekey_validation_key():
		pass

class PasswordHelper:
	def __init__(self, password):
		pass

	def _password_strength(self, password):
		pass

	def _is_strong_password(self, password):
		pass

	def _is_repeated_password(self, password):
		pass

	def _is_valid_password(self, password):
		pass

	def checkPassword(self, password):
		pass