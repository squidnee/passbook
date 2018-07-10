from faker import Faker
from random import choice
from passbook.features.orm import db
from passbook.models.users import User
from passbook.models.records import PasswordRecord, WalletRecord

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

def make_fake_password_records(user, count=25, faker=None):
	if not faker:
		faker = Faker()
	for i in range(count):
		record = PasswordRecord(name=faker.domain_name(), service_url=faker.url(), email=faker.safe_email(), username=faker.user_name())
		db.session.add(record)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
		db.session.rollback()

def make_fake_wallet_records(user, count=25, faker=None):
	if not faker:
		faker = Faker()
	for i in range(count):
		record_name = faker.iban()
		card_number = faker.credit_card_number()
		name_on_card = faker.name()
		security_code = faker.credit_card_security_code()
		expiry = faker.credit_card_expire()
		zip_code = faker.postcode()
		wallet = WalletRecord(name=record_name, card_number=card_number, name_on_card=name_on_card, expiration_date=expiry, \
			cvc_code=security_code, zip_code=zip_code)
		db.session.add(wallet)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
		db.session.rollback()

def make_fake_data(count=25):
	faker = Faker()
	user_results = db.session.query("""select * from user;""")
	if user_results:
		try:
			db.session.query(User).delete()
			db.session.commit()
		except Exception as e:
			print(e)
			db.session.rollback()
	user = User(username=faker.user_name(), email=faker.email(), password='mojo_jojo23')
	db.session.add(user)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
		db.session.rollback()
	make_fake_password_records(user, count=count, faker=faker)
	make_fake_wallet_records(user, count=count, faker=faker)
	print('Done making fake records!')