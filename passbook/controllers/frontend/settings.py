from flask import Blueprint, render_template
from flask import current_app as app

#settings = Blueprint('settings', __name__, url_prefix='/settings')

@app.route('/settings_basic')
def settings_basic():
	return render_template('settings/settings_basic.html')

@app.route('/settings_advanced')
def settings_advanced():
	return render_template('settings/settings_advanced.html')

@app.route('/user_preferences')
def user_preferences():
	return render_template('settings/user_preferences.html')