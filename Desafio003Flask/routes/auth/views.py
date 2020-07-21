from flask import render_template, request,url_for, redirect
from . import auth
from db.models import User
from flask_login import login_user, login_required, logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(senha):
            login_user(user,True)
            return redirect(url_for('main.login_index'))
    return render_template('auth/login.html')



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
