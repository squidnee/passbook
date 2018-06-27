from functools import wraps
from threading import Thread

def async_task(func):
	@wraps(func)
	def _decorated(*args, **kwargs):
		t = Thread(target=func, args=args, kwargs=kwargs)
		t.start()
	return _decorated