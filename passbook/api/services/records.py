import enum

from passbook.models.base import BaseModel
from passbook.models.records import PasswordRecord, WalletRecord, FileRecord
from passbook.models.notes import NoteRecord

class RecordType(enum.Enum):
	PasswordRecord = 1
	WalletRecord = 2
	FileRecord = 3
	NoteRecord = 4

class RecordService(BaseModel):
	__model__ = None
	
	def __init__(self, record_type):
		self.type = record_type

