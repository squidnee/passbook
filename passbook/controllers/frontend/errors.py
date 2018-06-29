# -*- coding: utf-8 -*-
"""
Handles application errors. Currently supports 404 errors, 500 errors, and raised error exceptions.
"""

from flask import render_template, request
from flask import current_app as app

@app.errorhandler(404)
def not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('errors/500.html'), 500

@app.errorhandler(Exception)
def exception_unhandled(e):
	app.logger.error('Unhandled Exception: %s', (e))
	return render_template('errors/500.html'), 500