from passbook.models.users import User

class UserHandler:

	@staticmethod
	def get_user(email):
		return User.query.filter_by(email=email).first()

	@staticmethod
	def get_user_by_id(id):
		return User.query.filter_by(id=id).first()

	@staticmethod
	def create_user(username, email, password):
		pass

	@staticmethod
	def edit_user():
		pass

	@staticmethod
	def delete_user():
		pass