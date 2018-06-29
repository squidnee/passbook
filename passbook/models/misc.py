from flask_sqlalchemy import SQLAlchemy

from ..app import db

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

class Family:
	pass

class Vault:
	pass

class MailCache:
	pass

class Tag(db.Model):
	tag_id = db.Column(db.Integer, primary_key=True)
	tag_name = db.Column(db.String(120), unique=True, nullable=False)