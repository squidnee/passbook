import enum

from datetime import datetime
from passbook.features.orm import db

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class ColorType(enum.Enum):
	Red = 1
	Orange = 2
	Yellow = 3
	Green = 4
	Blue = 5
	Purple = 6