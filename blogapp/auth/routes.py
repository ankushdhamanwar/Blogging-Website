from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_user, logout_user, login_required, current_user
from flask_security.utils import hash_password
from blogapp import db, user_datastore
from blogapp.models import User, Role


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name =  request.form['name']
        email = request.form['email']
        password = hash_password(request.form['password'])
        user = User.query.filter_by(email = email).first()
        if user:
            print("already exists")
            return redirect(url_for('auth.register'))
        else:
            user = user_datastore.create_user(email = email, password=password, name=name, roles=['author'])
            db.session.commit()
            login_user(user)
            return redirect(url_for('main.profile'))
    return render_template('signup.html')

# @auth.route('/signin', methods=['POST', 'GET'])
# def signin():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         user = User.query.filter_by(email = email).first()
#         if bcrypt.checkpw(password.encode('utf-8'), user.password):
#             login_user(user)
#             return redirect(url_for('main.profile'))
#         else:
#             return "wrong password"
#     return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

