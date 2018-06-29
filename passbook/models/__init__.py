from datetime import datetime
from ..app import db

class TimestampMixin(object):
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    accessed = db.Column(db.DateTime)

#from .records import Category
#from .users import *
#from .misc import *