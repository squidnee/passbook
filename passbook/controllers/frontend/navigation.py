from passbook.features.extensions import nav
from flask_nav.elements import *

@nav.navigation()
def navigation_bar():
	return Navbar(
		'Password Manager',
		View('Home', 'index'),
		View('Login', 'login'),
		View('Register', 'signup'),
		Subgroup('Current User',
			View('Settings', 'settings_basic'),
			View('Preferences', 'user_preferences'),
			Separator(),
			View('Logout', 'logout')
			)
		)