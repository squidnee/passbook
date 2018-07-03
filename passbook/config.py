# -*- coding: utf-8 -*-
"""
The configuration file. Controls the default application settings.
"""

import os

class BaseConfig(object):
	# General options
	DEBUG = True
	TESTING = False
	DEFAULT_URL = "127.0.0.1"
	PORT = 5000
	PYTHON_VERSION = "3.6.0"
	DEBUG_TB_INTERCEPT_REDIRECTS = False

	# Security options
	BCRYPT_LOG_ROUNDS = 12
	SALT_LENGTH = 32
	SESSION_TIMEOUT_MINUTES = 30
	CSRF_ENABLED = True

	# Database options
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Limits
	MAX_PASSWORD_LENGTH = 160
	MIN_PASSWORD_LENGTH = 6
	MAX_DESCRIPTION_LENGTH = 200
	MAX_NOTE_LENGTH = 500
	MAX_FAMILY_SIZE = 6

	# Form options
	WTF_CSRF_ENABLED = True

	# Mail options
	MAIL_FROM_EMAIL = "sydney@example.com"

	# Cache options
	ENTRY_CACHE_SIZE = 5

	# Compression options
	COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
	COMPRESS_LEVEL = 6
	COMPRESS_MIN_SIZE = 500

	# Organization options
	COLORS = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE", "PINK"]

	# File options
	UPLOAD_FOLDER = '../instance/uploads'
	MAX_CONTENT_LENGTH = 16 * 1024 * 1024

	# Filter options

class DevelopmentConfig(BaseConfig):
	DEVELOPMENT = True

class ProductionConfig(BaseConfig):
	DEBUG = False

class TestingConfig(BaseConfig):
	TESTING = True