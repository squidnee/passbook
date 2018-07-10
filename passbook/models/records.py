from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import event
from sqlalchemy_utils import JSONType, ScalarListType

from passbook.features.orm import db
from . import TimestampMixin
from .base import BaseTable

Base = declarative_base()

class Record(BaseTable):

	__tablename__ = 'record'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(128), unique=True, nullable=False)
	website = db.Column(db.String(128))
	email = db.Column(db.String(128))
	username = db.Column(db.String(128))
	#type
	#attrs
	#history
	#tags = relationship('Tag', secondary=tagging, backref='records')
	#attachments
	#notes
	#flags
	details = db.Column(JSONType)

	def __init__(self, name, website, username=None, password=None, email=None, notes=None, description=None):
		self.name = name
		self.website = website
		self.username = username
		self.password = password
		self.email = email
		self.description = description
		self.notes = notes

	def _get_name(self):
		return self.name
	def _get_owner_id(self):
		return self.owner_id
	def _get_website(self):
		return self.website
	def _get_username(self):
		return self.username
	def _get_email(self):
		return self.email
	def _get_description(self):
		return self.description
	def _get_notes(self):
		return self.notes
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	def update(self, properties):
		self.updated = datetime.utcnow()
		self.version += 1
	def update_credentials(self, creds):
		pass
	def delete(self):
		db.session.delete(self)
		db.session.commit()
	def save(self):
		db.session.add(self)
		db.session.commit()
	def encrypt(self):
		pass
	def decrypt(self):
		pass

	@staticmethod
	def get_all():
		return Record.query.all()

	def __repr__(self):
		return '<Site Record %r>' % self.name

class RecordAttributes(object):
	description = db.Column(db.String(200))
	starred = db.Column(db.Boolean, default=False)
	reprompt = db.Column(db.Boolean, default=False)
	color = db.Column(db.String(36))

class WalletRecord(TimestampMixin, db.Model):

	__tablename__ = 'wallet_records'

	id = db.Column(db.Integer, primary_key=True)
	card_name = db.Column(db.String(128), unique=True, nullable=False)
	card_type = db.Column(db.String(128))
	card_number = db.Column(db.Integer, nullable=False)
	name_on_card = db.Column(db.String(128), nullable=False)
	expiration_date = db.Column(db.Date, nullable=False)
	cvc_code = db.Column(db.Integer, nullable=False)
	zip_code = db.Column(db.Integer, nullable=False)
	description = db.Column(db.String(200)) #TODO: Update with config
	notes = db.Column(db.String(500)) #TODO: Update with config
	#TODO: tags

	def __init__(self, card_name, card_number, name_on_card, expiration_date, cvc_code, zip_code, description=None, notes=None):
		self.card_name = card_name
		self.card_number = card_number
		self.name_on_card = name_on_card
		self.expiration_date = expiration_date
		self.cvc_code = cvc_code
		self.zip_code = zip_code
		self.description = description
		self.notes = notes

	def __repr__(self):
		return '<Wallet Record %r>' % self.card_name

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class EncryptedFileRecord(BaseTable): #TODO: Finish

	__tablename__ = 'file'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(128))
	filename = db.Column(db.String(128))
	document = db.Column(db.LargeBinary, nullable=False)
	description = db.Column(db.String(200))
	notes = db.Column(db.String(500))

	def __init__(self, name, filename, document, description=None, notes=None):
		self.name = name
		self.filename = filename
		self.document = document
		self.description = description
		self.notes = notes

	def allowed_filename(self, filename):
		return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	def __repr__(self):
		return '<File %r>' % self.filename

class DecryptedFile: #TODO: Finish
	def __init__(self, name):
		self.name = name

class Tag(BaseTable):

	__tablename__ = 'tag'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), unique=True, nullable=False)

	def __init__(self, name=None):
		self.name = name

	def __repr__(self):
		return '<Tag %r>' % self.name