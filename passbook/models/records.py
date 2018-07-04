from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.hybrid import hybrid_property

from passbook.features.extensions import db
from . import TimestampMixin

class Category(db.Model):

	__tablename__ = 'categories'

	category_id = db.Column(db.Integer, primary_key=True)
	category_name = db.Column(db.String(50))
	site_records = db.relationship('SiteRecord', backref='categories')
	wallet_records = db.relationship('WalletRecord', backref='categories')
	file_records = db.relationship('EncryptedFileRecord', backref='categories')

	def __init__(self, category_name):
		self.category_name = category_name

	def __repr__(self):
		return '<Category %r>' % self.category_name

class SiteRecord(TimestampMixin, db.Model):

	__tablename__ = 'site_records'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), unique=True, nullable=False)
	owner_id = db.Column(db.String(32), nullable=False) #TODO
	category = db.Column(db.Integer, db.ForeignKey('categories.category_name'))
	website = db.Column(db.String(128), index=True, nullable=False)
	username = db.Column(db.String(64), index=True)
	password_hash = db.Column(db.String(128))
	description = db.Column(db.String(200)) #TODO: Update with config
	notes = db.Column(db.String(500)) #TODO: Update with config
	email = db.Column(db.String(120), index=True)
	expiration_date = db.Column(db.Date)
	version = db.Column(db.Integer, default=1)
	files = db.Column(db.LargeBinary)
	starred = db.Column(db.Boolean, default=False)
	reprompt = db.Column(db.Boolean, default=False)
	#TODO: tags, color, flags

	def __init__(self, name, owner_id, website, username=None, password=None, email=None, notes=None, description=None):
		self.name = name
		self.owner_id = owner_id
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
	def access(self):
		self.accessed = datetime.utcnow()
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
	def to_json(self):
		return jsonify({
			'id': self.id,
			'name': self.name,
			'owner_id': self.owner_id,
			'category': self.category,
			'website': self.website,
			'username': self.username,
			'email': self.email,
			'description': self.description,
			'notes': self.notes,
			'starred': self.starred,
			'files': self.files,
			'expiration_date': self.expiration_date,
			'version': self.version
			})

	@staticmethod
	def get_all():
		return SiteRecord.query.all()

	def __repr__(self):
		return '<Site Record %r>' % self.name

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
	category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
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

class EncryptedFileRecord(TimestampMixin, db.Model): #TODO: Finish

	__tablename__ = 'files'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	filename = db.Column(db.String(128))
	document = db.Column(db.LargeBinary, nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
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

class NoteRecord(TimestampMixin, db.Model):

	__tablename__ = 'notes'

	note_id = db.Column(db.Integer, primary_key=True)
	note_name = db.Column(db.String(128))
	files = db.Column(db.LargeBinary)
	starred = db.Column(db.Boolean, default=False)

class Folder(TimestampMixin, db.Model):

	__tablename__ = 'folders'

	folder_id = db.Column(db.Integer, primary_key=True)
	folder_name = db.Column(db.String(120), unique=True, nullable=False)
	parent_id = db.Column(db.String(120), default=None)
	#type [files, site_records, wallet_records, notes]
	#tags
	#tag_folder()
	#get_parent()
	#find()
	#move()
	#add_object()
	#add_folder()
	#add_folder()
	#delete_object()
	#delete_folder()
	#rename_folder()

	def __init__(self, folder_name, parent_id=None):
		self.folder_name = folder_name
		self.parent_id = parent_id

	def __repr__(self):
		return '<Folder %r>' % self.folder_name

class Tag(TimestampMixin, db.Model):

	__tablename__ = 'tags'

	tag_id = db.Column(db.Integer, primary_key=True)
	tag_name = db.Column(db.String(120), nullable=False)

	def __init__(self, tag_name):
		self.tag_name = tag_name

	def __repr__(self):
		return '<Tag %r>' % self.tag_name
	#add_tag()
	#add_color_to_tag()
	#edit_tag()
	#delete_tag()