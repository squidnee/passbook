from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from passbook.app import db
#from passbook.auth import login_manager as login
from . import TimestampMixin

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

	def __init__(self, username, email, plaintext_password):
		self.username = username
		self.email = email

	@hybrid_property
	def password(self):
		return self._master

	@password.setter
	def _set_password(self, plaintext):
		self._master = bcrypt.generate_password_hash(plaintext)

	def is_correct_password(self, plaintext):
		return bcrypt.check_password_hash(self._master, plaintext)

	def __repr__(self):
		return '<User {}>'.format(self.username)

#@login.user_loader
#def load_user(id):
#	return User.query.get(int(id))