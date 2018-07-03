from passbook.features.extensions import db
from passbook.models.users import User
#from passbook.forms.settings import UserPreferences

class UserManager:

	@staticmethod
	def get_user(email):
		return User.query.filter_by(email=email).first()

	@staticmethod
	def get_user_by_id(id):
		return User.query.filter_by(id=id).first()

	@staticmethod
	def create_user(username, email, password):
		if User.query.filter_by(email=email).first():
			return False

		elif User.query.filter_by(username=username).first():
			return False

		else:
			user = User(username=username, email=email, password=password)
			db.session.add(user)
			db.session.commit()
			return True

	@staticmethod
	def edit_user():
		pass

	@staticmethod
	def delete_user():
		pass

	@staticmethod
	def get_role():
		pass

	@staticmethod
	def get_trusted_users():
		pass

	@staticmethod
	def get_trusted_by():
		pass