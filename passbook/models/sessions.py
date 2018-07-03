from passbook.features.extensions import db
from . import TimestampMixin
from hashlib import sha256

ALPHABET = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def get_hexdigest(salt, plaintext):
	return sha256(salt + plaintext).hexdigest()

class Service(db.Model):
	service_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(32), unique=True, nullable=False)
	length = db.Column(db.Integer, default=8)
	symbols = db.Column(db.Boolean, default=True)
	alphabet = db.Column(db.String(32), default='')

	def __init__(self, name, length=8, symbols=True, alphabet=''):
		self.name = name
		self.length = length
		self.symbols = symbols
		self.alphabet = alphabet

	def get_alphabet(self):
		if self.alphabet:
			return self.alphabet
		alpha = ('abcdefghijklmnopqrstuvwxyz'
                 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '0123456789')
		if self.symbols:
			alpha += '!@#$%^&*()-_'
		return alpha

	def generate_password(self, plaintext):
		pass
