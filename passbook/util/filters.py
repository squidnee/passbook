## Query Filters ##
class QueryFilter:
	def __init__(self, field):
		self.field = field

class FilterLike(QueryFilter):
	def apply(self, query, value):
		if len(value) == 0:
			return query
		else:
			return query.filter(self.field.like("%%%s%%" % value.encode('utf-8').decode('utf-8')))

## Permissions ##
def check_perm(trusted_user, perm, record):
	return trusted_user.permissions[perm]

def can_reset_master_password(trusted_user):
	return check_perm(trusted_user=trusted_user, perm='RESET_MASTER_PASSWORD')

def can_add_records_all(trusted_user):
	return check_perm(trusted_user=trusted_user, perm='ADD_RECORDS_ALL')

def can_upload_files(trusted_user):
	return check_perm(trusted_user=trusted_user, perm='UPLOAD_FILES')

def can_sync_devices(trusted_user):
	return check_perm(trusted_user=trusted_user, perm='SYNC_DEVICES')

def can_view_record(trusted_user, record):
	return check_perm(trusted_user=trusted_user, perm='VIEW_CURR_RECORD', record=record)

def can_edit_record(trusted_user, record):
	return check_perm(trusted_user=trusted_user, perm='EDIT_CURR_RECORD', record=record)

def can_delete_record(trusted_user, record):
	return check_perm(trusted_user=trusted_user, perm='DELETE_CURR_RECORD', record=record)

def can_add_note(trusted_user, record):
	return check_perm(trusted_user=trusted_user, perm='ADD_NOTE_TO_CURR_RECORD', record=record)

## Template Filters ##