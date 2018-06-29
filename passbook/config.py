# -*- coding: utf-8 -*-
"""
The configuration file. Controls the default application settings.
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
	DEBUG = True
	TESTING = False
	RELOADER = True
	MAIL_FROM_EMAIL = "sydney@example.com"
	BCRYPT_LOG_ROUNDS = 12
	CSRF_ENABLED = True
	WTF_CSRF_ENABLED = True
	DEFAULT_URL = "127.0.0.1"
	PORT = 5000
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAX_PASSWORD_LENGTH = 160
	MIN_PASSWORD_LENGTH = 6
	MAX_DESCRIPTION_LENGTH = 200
	MAX_NOTE_LENGTH = 500
	SESSION_TIMEOUT_MINUTES = 30
	SALT_LENGTH = 32
	MAX_FAMILY_SIZE = 6
	ENTRY_CACHE_SIZE = 5
	ENVIRONMENT = property(lambda self: self.__class__.__name__)

class DevelopmentConfig(BaseConfig):
	DEVELOPMENT = True

class ProductionConfig(BaseConfig):
	DEBUG = False

class TestingConfig(BaseConfig):
	TESTING = True