# -*- coding: utf-8 -*-
"""
This is the application factory that will create the application instance, as well as a Celery app
to support asynchronous tasking.
"""

import os

from flask import Flask
from flask_migrate import Migrate
#from flask_sslify import SSLify
#from flask_cors import CORS
#from passbook.features.extensions import compress
from passbook.config import BaseConfig as Config

#BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def create_app(config=Config):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(config)
	app.config.from_pyfile('config.py')
	print(app.config)
	with app.app_context():
		#CORS(app)
		#SSLify(app)
		build_database(app)
		build_bootstrap(app)
		build_navigation_bar(app)
		build_mail(app)
		build_toolbar(app)
		add_csrf(app)
		#compress.init_app(app)
		register_endpoints()
		#register_post_extensions(app)
	return app

def build_database(app):
	from passbook.features.extensions import db
	db.init_app(app)
	migrate = Migrate(app, db)
	from passbook.models.records import SiteRecord
	from passbook.models.users import User
	db.create_all(app=app)

def build_bootstrap(app):
	from passbook.features.extensions import boot
	boot.init_app(app)

def build_navigation_bar(app):
	from passbook.features.extensions import nav
	nav.init_app(app)

def build_mail(app):
	from passbook.features.extensions import mail
	mail.init_app(app)

def build_toolbar(app):
	from passbook.features.extensions import toolbar
	toolbar.init_app(app)

def add_csrf(app):
	from passbook.features.extensions import csrf
	csrf.init_app(app)

def register_post_extensions(app):
	pass

def register_endpoints():
	## TODO : Set up assets with Flask-Assets
	## TODO : Set up SSL
	from passbook.controllers import frontend

def create_celery_app(app):
	from passbook.features.tasks import celery
	celery.conf.update(app.config)
	TaskBase = celery.Task
	class ContextTask(TaskBase):
		abstract = True
		def __call__(self, *args, **kwargs):
			with app.app_context():
				return TaskBase.__call__(self, *args, **kwargs)
	celery.Task = ContextTask
	return celery