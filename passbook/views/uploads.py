import os
from flask import current_app as app
from flask import Blueprint, send_from_directory, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from passbook.models.records import EncryptedFileRecord

uploads_bp = Blueprint('uploads', __name__, url_prefix='/uploads')

# TODO: Finish
# http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
@uploads_bp.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			flash('OK file!')

@uploads_bp.route('/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)