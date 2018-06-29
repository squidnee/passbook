from flask import Flask, render_template, redirect, url_for, flash#, session
from flask_login import login_required, login_user, logout_user#, LoginManager
from flask import current_app as app

from passbook.auth import login_manager
from passbook.forms.auth_forms import MasterPasswordForm, SignUpForm
#from ..models.users import User

# Redirects to the login form if user is not logged in
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'auth.login'

## TODO : Make this route available over secure HTTP
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MasterPasswordForm()
    if form.validate_on_submit():
        flash(u'Successfully logged in.')
        return redirect(url_for('index'))
    return render_template("auth/login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('User was logged out.')
    return redirect(url_for('index'))

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        #db.session.add(user)
        #db.session.commit()
        return redirect(url_for('index'))
    return render_template('auth/signup.html', form=form)