from passbook.extensions import nav
from flask_nav.elements import *

@nav.navigation()
def navigation_bar():
	return Navbar(
		View('Home', 'index'),
		View('Login', 'login'),
		View('Sign Up', 'signup')
		)