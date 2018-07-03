from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

from passbook.extensions import db
from . import TimestampMixin

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)

	def __repr__(self):
		return '<Category %r>' % self.name

class Record(TimestampMixin, db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), unique=True, nullable=False)
	owner = db.Column(db.String(32), nullable=False) #TODO
	category = db.Column(db.Integer, nullable=False)
	website = db.Column(db.String(128), index=True, nullable=False)
	username = db.Column(db.String(64), index=True, unique=False)
	password = db.Column(db.String(128))
	password_hash = db.Column(db.String(128))
	description = db.Column(db.String(200)) #TODO: Update with config
	notes = db.Column(db.String(500)) #TODO: Update with config
	email = db.Column(db.String(120), index=True, unique=False)
	expiration_date = db.Column(db.Date)
	version = db.Column(db.Integer, default=1)
	files = db.Column(db.LargeBinary)
	starred = db.Column(db.Boolean, default=False)
	reprompt = db.Column(db.Boolean, default=False)
	#TODO: tags, color

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	def update(self, properties):
		self.updated = datetime.utcnow()
		self.version += 1
	def update_credentials(self, creds):
		pass
	def access(self):
		self.accessed = datetime.utcnow()
	def reset(self):
		pass
	def encrypt(self):
		pass
	def decrypt(self):
		pass
	def to_json(self):
		pass

	def __repr__(self):
		return '<Record %r>' % self.name

class WalletRecord(TimestampMixin, db.Model):

	id = db.Column(db.Integer, primary_key=True)
	card_name = db.Column(db.String(128))
	card_type = db.Column(db.String(128))
	card_number = db.Column(db.Integer, nullable=False)
	name_on_card = db.Column(db.String(128), nullable=False)
	expiration_date = db.Column(db.Date, nullable=False)
	secret_code = db.Column(db.Integer, nullable=False)
	zip_code = db.Column(db.Integer)
	description = db.Column(db.String(200)) #TODO: Update with config
	notes = db.Column(db.String(500)) #TODO: Update with config
	#TODO: tags

class EncryptedDocumentRecord(db.Model): #TODO: Finish

	id = db.Column(db.Integer, primary_key=True)
	document = db.Column(db.LargeBinary, nullable=False)

	def __repr__(self):
		return '<Document %r>' % self.name

class DecryptedDocument: #TODO: Finish
	def __init__(self, name):
		self.name = name