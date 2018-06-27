import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = True
	TESTING = False
	MAIL_FROM_EMAIL = "sydney@example.com"
	BCRYPT_LOG_ROUNDS = 12

class DevelopmentConfig(Config):
	DEVELOPMENT = True

class ProductionConfig(Config):
	DEBUG = False

class TestingConfig(Config):
	TESTING = True