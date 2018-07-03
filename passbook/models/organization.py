from passbook.features.extensions import db
from . import TimestampMixin

class Folder(TimestampMixin, db.Model):
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

class Tag(TimestampMixin, db.Model):
	tag_id = db.Column(db.Integer, primary_key=True)
	tag_name = db.Column(db.String(120), unique=True, nullable=False)
	#add_tag()
	#add_color_to_tag()
	#edit_tag()
	#delete_tag()