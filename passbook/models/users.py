import jwt

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
#from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

#from passbook.app import db
#from passbook.auth import login_manager as login
from . import TimestampMixin, db

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

class Permissions:
	GENERAL = 0x01
	ADMIN = 0xff

class User(UserMixin, TimestampMixin, db.Model):

	#__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(32), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	is_manager = db.Column(db.Boolean, default=False) # Unless first entry
	trusted_by = db.Column(db.String(32), unique=True)
	trusts = db.Column(db.String(32), unique=True)

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
		return '<User {}>'.format(self.username)

class UserPreferences:
	pass

#@login.user_loader
#def load_user(id):
#	return User.query.get(int(id))