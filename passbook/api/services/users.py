import jwt

from passbook.models.base import BaseModel
from passbook.models.users import User

class UserService(BaseModel):
	__model__ = User

	def __init__(self, app=None):
		self.jwt_algorithm = 'HS256'
		self.reset_password_token_expiration_time = 600

		if app:
			self.load_from_config(app)

	def load_from_config(self, app=None):
		cfg = app.config

	def save(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass

	def login(self):
		pass

	def logout(self):
		pass

	def register(self):
		pass

	def change_email(self):
		pass

	def reset_email(self):
		pass

	def change_password(self):
		pass

	def confirm_email(self):
		pass

	def get_email_confirmation(self):
		pass
