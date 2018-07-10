import os
from flask import current_app as app
from flask import send_from_directory, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from passbook.models.records import FileRecord
from passbook.forms.records import FileUploadForm

# TODO: Finish
# http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
@app.route('/upload_file_record', methods=['GET', 'POST'])
def upload_file():
	form = FileUploadForm()
	for i in xrange(5):
		form.uploads.append_entry()
	file_data = []
	if form.validate_on_submit():
		for file_entry in form.uploads.entries:
			file_data.append(file_entry)
	return render_template("dashboard/index.html", form=form, file_data=file_data)

@app.route('/file_record/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)