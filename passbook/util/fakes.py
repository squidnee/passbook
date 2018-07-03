from faker import Faker
from passbook.extensions import db
from passbook.models.users import User
from passbook.models.records import Record

def make_fake_users(count=25):
	faker = Faker()
	for i in range(count):
		user = User(username=faker.user_name(),
				email=faker.email(),
				password='password')
		db.session.add(user)
		try:
			db.session.commit()
		except:
			db.session.rollback()


def make_fake_records(count=25):
	pass

def make_fake_records_wallet(count=25):
	pass