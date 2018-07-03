from passbook.features.extensions import db
from . import TimestampMixin

class Device(db.Model):
	device_id = db.Column(db.Integer, primary_key=True)
	#make
	model = db.Column(db.String(120), unique=True, nullable=False)
	#client_name
	#client_version
	os_name = db.Column(db.String(120), unique=True, nullable=False)
	#os_version
	#last_auth_ip
	#user_agent

class Folder(TimestampMixin, db.Model):
	folder_id = db.Column(db.Integer, primary_key=True)
	folder_name = db.Column(db.String(120), unique=True, nullable=False)
	parent_id = db.Column(db.String(120), default=None)
	#type [files, records, wallet_records]
	#tags
	#tag_folder()
	#get_parent()
	#find()
	#move()
	#add_object()
	#delete_object()

class Family:
	pass

class Vault:
	pass

class MailCache:
	pass

class Tag(TimestampMixin, db.Model):
	tag_id = db.Column(db.Integer, primary_key=True)
	tag_name = db.Column(db.String(120), unique=True, nullable=False)