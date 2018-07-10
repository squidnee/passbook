import os
import re
import base64
import string
import random
import struct

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random as CryptoRandom

from hashlib import sha256

## Variables ##
ALPHABET = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

## Methods ##

# These methods taken from here: https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto/
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
	if not out_filename:
		out_filename = in_filename + '.enc'

	iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	size = os.path.getsize(in_filename)

	with open(in_filename, 'rb') as infile:
		with open(out_filename, 'wb') as outfile:
			outfile.write(struct.pack('<Q', size))
			outfile.write(iv)

			while True:
				chunk = infile.read(chunksize)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - len(chunk) % 16)

				outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
	if not out_filename:
		out_filename = os.path.splitext(in_filename)[0]

	with open(in_filename, 'rb') as infile:
		origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
		iv = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, iv)

		with open(out_filename, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)
				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(origsize)

def password_strength(password, length=8):
	flags = []
	flag_dict = {
		"LENGTH_FLAG": "Passwords must be greater than expected length.",
		"NO_DIGITS_FLAG": "Password must contain digits.",
		"NO_UPPERCASE_FLAG": "Passwords must contain at least one uppercase letter.",
		"NO_LOWERCASE_FLAG": "Passwords must contain at least one lowercase letter.",
		"NO_SYMBOLS_FLAG": "Passwords must contain at least one special symbol."
	}
	if len(password) < length:
		flags.append("LENGTH_FLAG")
	if re.search(r"\d", password) is None:
		flags.append("NO_DIGITS_FLAG")
	if re.search(r"[A-Z]", password) is None:
		flags.append("NO_UPPERCASE_FLAG")
	if re.search(r"[a-z]", password) is None:
		flags.append("NO_LOWERCASE_FLAG")
	if re.search(r"[ !#$%&'(@)*+,-./[\\\]^_`{|}~"+r'"]', password) is None:
		flags.append("NO_SYMBOLS_FLAG")
	return len(flag_dict.keys()) - len(flags)

def get_hexdigest(salt, plaintext):
	return sha256(salt + plaintext).hexdigest()

def make_password(plaintext, service):
	salt = get_hexdigest(secret_key, service)[:20]
	hsh = get_hexdigest(salt, plaintext)
	return ''.join((salt, hsh))

def password(plaintext, service, length=10, alphabet=ALPHABET):
	raw_hexdigest = make_password(plaintext, service)
	num = int(raw_hexdigest, 16)
	num_chars = len(alphabet)
	chars = []
	while len(chars) < length:
		num, idx = divmod(num, num_chars)
		chars.append(alphabet[idx])
	return ''.join(chars)

## Classes ##

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