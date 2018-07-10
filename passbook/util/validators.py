from wtforms.validators import ValidationError, Required, Email, Length, Regexp, EqualTo

class Unique(object):
    def __init__(self, model, field, message=u'This element already exists.'):
        self.model = model
        self.field = field

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

validators = {
	'email': [Required(), Email()],
	'password': [Required(), Length(min=6, max=50), EqualTo('repeat_password', message='Passwords must match'), \
	Regexp(r'[A-Za-z0-9@#$%^&+=]',message='Password contains invalid characters')]
}