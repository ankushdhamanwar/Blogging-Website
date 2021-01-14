from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import current_user, login_required, roles_required, roles_accepted
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post')
def post():
    return render_template('post.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/profile')
# @login_required
# @roles_required('admin')
# @roles_accepted('admin', 'author')
def profile():
    return render_template('profile.html')