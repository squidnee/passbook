from flask import current_app as app

from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, LoginManager

from forms import MasterPasswordForm, SignUpForm
from models import User

## TODO : Forgot Password implementation --> https://exploreflask.com/en/latest/users.html

## TODO: Check session expiration status?

#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view =  "index"

@app.route('/')
#@login_required
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MasterPasswordForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)