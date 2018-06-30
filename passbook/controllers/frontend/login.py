from flask import Flask, render_template, redirect, url_for, flash, request#, session
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app as app

#from passbook.auth import login_manager
from passbook.extensions import db
from passbook.forms.auth import LoginForm, SignUpForm, ResetPasswordForm, ResetPasswordRequestForm
from passbook.models.users import User
from passbook.api.handlers.users import UserHandler
from passbook.mail import send_password_reset_email

from werkzeug.urls import url_parse
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_accessed = datetime.utcnow()
        db.session.commit()

## TODO : Make this route available over secure HTTP
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("auth/login.html", title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('User was logged out.')
    return redirect(url_for('login'))

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        password = form.password.data
        user = User(username=form.username.data, email=form.email.data, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth/signup.html', title='Sign Up', form=form)

@app.route('/reset_password_request', methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('auth/reset_password_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user._set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('auth/reset_password.html', form=form)