from flask import render_template
from flask import current_app as app

@app.route('/list_trusted_users')
def list_trusted_users():
	pass

@app.route('/add_trusted_user', methods=['GET', 'POST'])
def add_trusted_user():
	pass