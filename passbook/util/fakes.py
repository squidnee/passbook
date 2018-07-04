from faker import Faker
from random import choice
from passbook.features.extensions import db
from passbook.models.users import User
from passbook.models.records import SiteRecord

def get_random_category():
	categories = ['work', 'travel', 'finance', 'social media', 'shopping', 'news', 'personal', 'health', 'other']
	return choice(categories)

def make_fake_user():
	faker = Faker()
	user = User(username=faker.user_name(),
				email=faker.email(),
				password='password')
	db.session.add(user)
	try:
		db.session.commit()
	except:
		db.session.rollback()


def make_fake_records(user, count=25):
	faker = Faker()
	for i in range(count):
		record = SiteRecord(name=faker.domain_name(), 
							owner_id=user.id, 
							website=faker.url(), email=faker.safe_email(), username=faker.user_name())
		db.session.add(record)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
		db.session.rollback()

def make_fake_data(count=25):
	faker = Faker()
	user = User(username=faker.user_name(), email=faker.email(), password='mojo_jojo23')
	db.session.add(user)
	db.session.commit()
	make_fake_records(user, count=count)
	print('Done making fake records!')