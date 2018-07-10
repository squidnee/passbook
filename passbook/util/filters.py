class QueryFilter:
	def __init__(self, field):
		self.field = field

class FilterLike(QueryFilter):
	def apply(self, query, value):
		if len(value) == 0:
			return query
		else:
			return query.filter(self.field.like("%%%s%%" % value.encode('utf-8').decode('utf-8')))