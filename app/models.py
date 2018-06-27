from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()

class TimestampMixin(object):
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	_master = db.Column(db.String(128), nullable=False)
	authenticated = db.Column(db.Boolean, default=False)

	def __init__(self, email, plaintext_password):
		self.email = email
		self._master = plaintext_password
		self.authenticated = False

	@hybrid_property
	def password(self):
		return self._master

	@password.setter
	def _set_password(self, plaintext):
		self._master = bcrypt.generate_password_hash(plaintext)

	def is_correct_password(self, plaintext):
		return bcrypt.check_password_hash(self._master, plaintext)

	def __repr__(self):
		return '<id {}>'.format(self.id)

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)

	def __repr__(self):
		return '<Category %r>' % self.name

class LoginCredential(TimestampMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
	service = db.Column(db.String(64), index=True, nullable=False)
	username = db.Column(db.String(64), index=True, unique=False)
	password_hash = db.Column(db.String(128))
	email = db.Column(db.String(120), index=True, unique=False)
	notes = db.Column(db.String(300), index=True, unique=False)
	created = db.Column(db.DateTime, nullable=False, default=datetime.now)
	updated = db.Column(db.DateTime, onupdate=datetime.now)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	def update(self, properties):
		self.parent().last_updated = datetime.now()
	def reset(self):
		pass

class WalletCredential(TimestampMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)