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
		register_endpoints(app)
		create_logger(app)
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

def register_endpoints(app):
	## TODO : Set up assets with Flask-Assets
	## TODO : Set up SSL
	from passbook.views import errors, login, navigation, records, settings, uploads
	from passbook.views.records import records_bp
	from passbook.views.uploads import uploads_bp
	app.register_blueprint(records_bp, url_prefix='/records')
	app.register_blueprint(uploads_bp, url_prefix='/uploads')

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

def create_logger(app):
	if not app.config['DEBUG']:
		from passbook.features.logging import return_file_logger
		file_handler = return_file_logger()
		app.logger.addHandler(file_handler)
		app.logger.setLevel(logging.INFO)
		app.logger.info('Password Manager logging')