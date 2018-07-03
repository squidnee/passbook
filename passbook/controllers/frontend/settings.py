from flask import render_template
from flask import current_app as app

@app.route('/settings_basic')
def settings_basic():
	return render_template('settings/settings_basic.html')

@app.route('/settings_advanced')
def settings_advanced():
	return render_template('settings/settings_advanced.html')

@app.route('/user_preferences')
def user_preferences():
	return render_template('settings/user_preferences.html')