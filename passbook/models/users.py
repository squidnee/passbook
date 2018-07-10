import jwt

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask import current_app as app
from flask_login import UserMixin
#from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_utils import IPAddressType

from passbook.features.orm import db
from . import TimestampMixin
from .base import BaseTable

#basic_auth = HTTPBasicAuth()
#token_auth = HTTPTokenAuth()

class Permissions:
	GENERAL = 0x01
	ADMIN = 0xff

class User(UserMixin, BaseTable):

	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False, index=True)
	password_hash = db.Column(String(128))
	#devices
	#preferences
	#history

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self._set_password(password)

	def _set_password(self, plaintext):
		self.password_hash = generate_password_hash(plaintext)

	def is_correct_password(self, plaintext):
		return check_password_hash(self.password_hash, plaintext)

	def get_reset_password_token(self, expires_in=600):
		return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in}, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

	@staticmethod
	def verify_reset_password_token(token):
		try:
			id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
		except:
			return
		return User.query.get(id)

	def __repr__(self):
		return '<User %r>' % (self.username)

class UserPreferences(BaseTable):

	__tablename__ = 'user_preferences'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	phone_number = db.Column(db.String(64))
	password_hint = db.Column(db.String(128))
	#language
	#timezone
	#trusted_users

	def __init__(self, first_name=None, last_name=None, phone_number=None, password_hint=None):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number
		self.password_hint = password_hint

	def __repr__(self):
		return '<UserPreferences %r>' % (self.id)

class Device(BaseTable):

	__tablename__ = 'device'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	make = db.Column(db.String(120))
	model = db.Column(db.String(120))
	client_name = db.Column(db.String(120))
	#client_version
	os_name = db.Column(db.String(120))
	#os_version
	last_auth_ip = db.Column(IPAddressType)
	#user_agent

	def __init__(self, name=None, make=None, model=None, client_name=None, os_name=None):
		self.name = name
		self.make = make
		self.model = model
		self.client_name = client_name
		self.os_name = os_name

	def __repr__(self):
		return '<Device %r>' % (self.name)


class TrustedUser:
	def can(self):
		pass