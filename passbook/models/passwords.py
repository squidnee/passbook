from passbook.features.orm import db
from . import TimestampMixin
from hashlib import sha256
from sqlalchemy_utils import ScalarListType

ALPHABET = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def get_hexdigest(salt, plaintext):
	return sha256(salt + plaintext).hexdigest()

class PasswordItemClient(db.Model):

	__tablename__ = 'passwords'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	record_id = db.Column(db.Integer)
	username = db.Column(db.String(32))
	#password = 
	email = db.Column(db.String(32))
	#service =

class PasswordItem(PasswordItemClient):
	digest_key = db.Column(db.String(64))
	salt = db.Column(db.String(32))
	length = db.Column(db.Integer)
	#encryption
	#history
	flags = db.Column(ScalarListType())

class Service(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	service_name = db.Column(db.String(32), unique=True, nullable=False)
	domain_name = db.Column(db.String(32), unique=True, nullable=False)
	length = db.Column(db.Integer, default=8)
	symbols = db.Column(db.Boolean, default=True)
	alphabet = db.Column(db.String(32), default='')
	equiv_domains = db.Column(ScalarListType())

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

class ServicePasswordRules(db.Model):
	service_id = db.Column(db.Integer, primary_key=True)
	symbols = db.Column(db.Boolean, default=True)
	alphabet = db.Column(db.String(32), default='')
	min_password_length = db.Column(db.Integer, default=8)
	max_password_length = db.Column(db.Integer, default=None)
	min_required_uppercase = db.Column(db.Integer, default=None)
	min_required_numbers = db.Column(db.Integer, default=None)
	min_required_special_chars = db.Column(db.Integer, default=None)
