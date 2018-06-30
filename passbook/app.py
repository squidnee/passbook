# -*- coding: utf-8 -*-
"""
This is the application factory that will create the application instance, as well as a Celery app
to support asynchronous tasking.
"""

import os

from flask import Flask
from flask_migrate import Migrate
from .extensions import db, mail, csrf, compress, toolbar, boot, nav#, api
from .config import BaseConfig as Config

#BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_app(config=Config):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(config)
	app.config.from_pyfile('config.py')
	with app.app_context():
		register_pre_extensions(app)
		build_database()
		register_endpoints()
		#register_post_extensions(app)
	return app

def register_pre_extensions(app):
	db.init_app(app)
	Migrate(app, db)
	boot.init_app(app)
	nav.init_app(app)
	mail.init_app(app)
	compress.init_app(app)
	csrf.init_app(app)
	toolbar.init_app(app)

def build_database():
	from passbook.models.records import Record
	from passbook.models.users import User
	db.create_all()

def register_post_extensions(app):
	#api.init_app(app)
	pass

def register_endpoints():
	## TODO : Set up assets with Flask-Assets
	## TODO : Set up SSL
	from passbook.controllers import frontend
	from passbook.controllers import resources

def create_celery_app(app):
	from .extensions import celery
	celery.conf.update(app.config)
	TaskBase = celery.Task
	class ContextTask(TaskBase):
		abstract = True
		def __call__(self, *args, **kwargs):
			with app.app_context():
				return TaskBase.__call__(self, *args, **kwargs)
	celery.Task = ContextTask
	return celery