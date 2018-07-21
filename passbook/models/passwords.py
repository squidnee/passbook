from passbook.features.orm import db
from passbook.util.security import password as get_password_wrapper
from hashlib import sha256
from sqlalchemy_utils import ScalarListType
from .base import BaseTable

class PasswordItem(BaseTable):

	__tablename__ = 'passwords'

	digest_key = db.Column(db.String(64))
	salt = db.Column(db.String(32))
	length = db.Column(db.Integer)
	#encryption
	#history
	flags = db.Column(ScalarListType())

class Service(db.Model):

	__tablename__ = 'services'

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

	def get_password(self, plaintext):
		return get_password_wrapper(plaintext, self.name, self.length, self.get_alphabet())

	def generate_password(self, plaintext):
		pass

	@classmethod
	def search(cls, query):
		return cls.select().where(cls.name ** ('%%%s%%' % query))

class ServicePasswordRules(db.Model):
	service_id = db.Column(db.Integer, primary_key=True)
	symbols = db.Column(db.Boolean, default=True)
	alphabet = db.Column(db.String(32), default='')
	min_password_length = db.Column(db.Integer, default=8)
	max_password_length = db.Column(db.Integer, default=None)
	min_required_uppercase = db.Column(db.Integer, default=None)
	min_required_numbers = db.Column(db.Integer, default=None)
	min_required_special_chars = db.Column(db.Integer, default=None)
