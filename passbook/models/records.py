import os
import enum
import json

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import event
from sqlalchemy.orm import relationship, backref
#from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy_utils import JSONType, ScalarListType

from passbook.features.orm import db
from passbook.util.security import encrypt_file, decrypt_file
from passbook.models import NOTE_FIELDS
from passbook.models.base import BaseTable

Base = declarative_base()

tag_table = db.Table('tags', Base.metadata, db.Column('password_record_id', db.Integer, db.ForeignKey('password_records.id')),
	db.Column('wallet_record_id', db.Integer, db.ForeignKey('wallet_records.id')),
		db.Column('file_record_id', db.Integer, db.ForeignKey('file_records.id')),
		db.Column('note_record_id', db.Integer, db.ForeignKey('note_records.id'))
		)

class Record(BaseTable):

	__tablename__ = 'records'

	name = db.Column(db.String(128), unique=True, nullable=False)
	description = db.Column(db.String(200))
	starred = db.Column(db.Boolean, default=False)
	reprompt = db.Column(db.Boolean, default=False)
	color = db.Column(db.String(36))
	notes = db.Column(db.String(128))
	details = db.Column(JSONType())
	attachments = db.Column(ScalarListType())
	history = db.Column(ScalarListType())
	type = db.Column(db.String(50))

	__mapper_args__ = {
		'polymorphic_identity':'records',
		'polymorphic_on': type
	}

	def _get_name(self):
		return self.name
	def _get_description(self):
		return self.description
	def _get_starred(self):
		return self.starred
	def _get_reprompt(self):
		return self.reprompt
	def _get_color(self):
		return self.color
	def _get_notes(self):
		return self.notes
	def _get_flags(self):
		pass
	def _get_tags(self):
		pass
	def _get_attachments(self):
		pass
	def _get_history(self):
		pass

	def change_description(self):
		pass

	def change_color(self):
		pass

class PasswordRecord(Record):

	__tablename__ = 'password_records'

	id = db.Column(db.Integer, db.ForeignKey('records.id'), primary_key=True)
	service_name = db.Column(db.String(128))
	service_url = db.Column(db.String(128))
	service_domain = db.Column(db.String(64))
	email = db.Column(db.String(128))
	username = db.Column(db.String(128))
	password = db.Column(db.String(128))

	__mapper_args__ = {'polymorphic_identity': 'password_records'}

	def __init__(self, name=None, service_name=None, service_url=None, service_domain=None, username=None, password=None, email=None, notes=None, description=None, reprompt=None):
		self.name = name
		self.service_name = service_name
		self.service_url = service_url
		self.service_domain = service_domain
		self.username = username
		self.password = password
		self.email = email
		self.description = description
		self.notes = notes
		self.reprompt = reprompt

	def _get_service_name(self):
		return self.service_name
	def _get_service_domain(self):
		return self.service_domain
	def _get_service(self):
		pass
	def _get_username(self):
		return self.username
	def _get_email(self):
		return self.email
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	def delete(self):
		db.session.delete(self)
		db.session.commit()
	def save(self):
		db.session.add(self)
		db.session.commit()

	def __repr__(self):
		return '<PasswordRecord %r>' % self.name

class WalletRecord(Record):

	__tablename__ = 'wallet_records'

	id = db.Column(db.Integer, db.ForeignKey('records.id'), primary_key=True)
	card_type = db.Column(db.String(128))
	card_number = db.Column(db.Integer, nullable=False)
	name_on_card = db.Column(db.String(128), nullable=False)
	expiration_date = db.Column(db.String(5), nullable=False)
	cvc_code = db.Column(db.Integer, nullable=False)
	zip_code = db.Column(db.Integer, nullable=False)

	__mapper_args__ = {'polymorphic_identity': 'wallet_records'}

	def __init__(self, name, card_number, name_on_card, expiration_date, cvc_code, zip_code, description=None, notes=None):
		self.name = name
		self.card_number = card_number
		self.name_on_card = name_on_card
		self.expiration_date = expiration_date
		self.cvc_code = cvc_code
		self.zip_code = zip_code
		self.description = description
		self.notes = notes

	def __repr__(self):
		return '<WalletRecord %r>' % self.card_name

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class FileRecord(Record):

	__tablename__ = 'file_records'

	id = db.Column(db.Integer, db.ForeignKey('records.id'), primary_key=True)
	encrypted_filename = db.Column(db.String(128))
	unencrypted_filename = db.Column(db.String(128))
	extension = db.Column(db.String(6))
	encrypted_content = db.Column(db.LargeBinary)
	file_path = db.Column(db.String(128))
	parent_id = db.Column(db.Integer, default=None)
	unencrypted_file_size = db.Column(db.Integer)

	__mapper_args__ = {'polymorphic_identity': 'file_records'}

	def __init__(self, name=None, encrypted_filename=None, unencrypted_filename=None, unencrypted_content=None, file_path=None, description=None, notes=None):
		self.name = name
		self.encrypted_filename = encrypted_filename
		self.file_path = file_path
		self.description = description
		self.notes = notes
		self.unencrypted_file_size = os.path.getsize(unencrypted_filename) if unencrypted_filename else None

		encrypt_file(in_filename=unencrypted_filename, out_filename=encrypted_filename)

	def allowed_filename(self, filename):
		return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	def set_extension(self, filename):
		pass

	def decrypt(self, in_filename=None, out_filename=None):
		if not in_filename:
			in_filename = self.encrypted_filename

		if not out_filename:
			out_filename = self.unencrypted_filename

		decrypt_file(in_filename, out_filename)

	def __repr__(self):
		return '<FileRecord %r>' % self.encrypted_filename

class NoteRecord(Record):

	__tablename__ = 'note_records'

	id = db.Column(db.Integer, db.ForeignKey('records.id'), primary_key=True)
	note_type = db.Column(db.String(64))
	fields = db.Column(JSONType)

	__mapper_args__ = {'polymorphic_identity': 'note_records'}

	def __init__(self, name, note_type=None):
		self.name = name
		if not note_type:
			self.note_type = "Blank"
			self.fields = {}
		else:
			assert note_type in NOTE_FIELDS
			self.note_type = note_type
		try:
			self.fields = json.loads(NOTE_FIELDS[note_type])
		except Exception as e:
			print(e)

	def __repr__(self):
		return '<NoteRecord %r>' % self.name

class Tag(db.Model):

	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	password_record_id = db.Column(db.Integer,db.ForeignKey('password_records.id'))
	wallet_record_id = db.Column(db.Integer,db.ForeignKey('wallet_records.id'))
	file_record_id = db.Column(db.Integer,db.ForeignKey('file_records.id'))
	note_record_id = db.Column(db.Integer,db.ForeignKey('note_records.id'))

	def __init__(self, name=None):
		self.name = name

	@property
	def serialize(self):
		return {
		'id': self.id,
		'name': self.name
		}

	def __repr__(self):
		return '<Tag %r>' % self.name

class Flag(db.Model):

	__tablename__ = 'flags'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	description = db.Column(db.String(200), unique=True, nullable=False)

	def __init__(self, name, description):
		self.name = name
		self.description = description

	@property
	def serialize(self):
		return {
		'id': id,
		'name': name
		}

	def __repr__(self):
		return '<Flag %r>' % self.name
