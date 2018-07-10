import json
import logging

from datetime import datetime
from flask import current_app as app
from sqlalchemy.ext.declarative import DeclarativeMeta
from passbook.features.orm import db

class BaseModel:
	__model__ = None

	def is_instance(self, model):
		return isinstance(model, self.__model__)

	def save(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass

	def get_by_id(self, id):
		return self.__model__.query.get(id)

	def find(self, **kwargs):
		return self.__model__.query.filter_by(**kwargs).all()

	def find_first(self, **kwargs):
		return self.__model__.query.filter_by(**kwargs).first()

	def log(self, message, level=None):
		level = logging.INFO if not level else level
		app.logger.log(msg=message, level=level)

class BaseTable(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	last_accessed = db.Column(db.DateTime)
	version = db.Column(db.Integer, default=1)

	def save(self):
		db.session.add(self)
		db.session.flush()

	def update(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)
		self.save()

	@classmethod
	def find(cls_, **kwargs):
		query = db.session.query(cls_)
		if kwargs is not None:
			for k, v in kwargs.items():
				if isinstance(v, list):
					query = query.filter(getattr(cls_, k).in_(v))
				else:
					query = query.filter(getattr(cls_, k) == v)
		return query

	@classmethod
	def find_first(cls_, **kwargs):
		return cls_.find(**kwargs).first()

	@classmethod
	def delete(cls_, args):
		query = db.session.query(cls_)
		for k, v in args.items():
			query = query.filter(getattr(cls_, k) == v)
		query.delete()

	def encrypt(self):
		pass

	def decrypt(self):
		pass

	def as_dict(self):
		fields = {}
		for col in self.__table__.columns:
			fields[col.name] = getattr(self, col.name)
		return fields

	def import_from_json(self):
		pass

	def export_to_json(self):
		pass

	def log(self, message, level=None):
		level = logging.INFO if not level else level
		app.logger.log(msg=message, level=level)
