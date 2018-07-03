import os
import logging

from logging.handlers import RotatingFileHandler

def return_file_logger(handler_name='logs/passbook.log'):
	if not os.path.exists('../instance/logs'):
		os.mkdir('../instance/logs')
	file_handler = RotatingFileHandler(handler_name, maxBytes=10240, backupCount=10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	file_handler.setLevel(logging.INFO)
	return file_handler