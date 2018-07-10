import enum

from passbook.features.orm import db
from passbook.models.records import Record

NOTE_TYPES = [
	"Passport",
	"Driver's License",
	"Wifi",
	"Bank Account",
	"Instant Messenger",
	"Health Insurance",
	"Membership",
	"Database",
	"Server",
	"Email Account",
	"Mobile Contact",
	"Legal Document",
	"SSN"
]

class NoteRecord(Record):

	__tablename__ = 'note_records'

	note_type = db.Column(db.String(64))