from flask_wtf import Form

# TODO: CSRF protection --> http://flask.pocoo.org/snippets/3/
# TODO: Move this to core.py?

class BaseForm(Form):
    def __iter__(self):
        token = self.csrf_token
        yield token

        field_names = {token.name}
        for cls in self.__class__.__bases__:
            for field in cls():
                field_name = field.name
                if field_name not in field_names:
                    field_names.add(field_name)
                    yield self[field_name]

        for field_name in self._fields:
            if field_name not in field_names:
                yield self[field_name]