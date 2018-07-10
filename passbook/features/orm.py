import logging

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create():
	db.create_all()

def rebuild():
	db.drop_all()
	create()