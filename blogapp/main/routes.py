from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import current_user, login_required, roles_required, roles_accepted
from blogapp.models import User, Post, UserRoles, Role
from blogapp import db
main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template('index.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/profile')
@login_required
@roles_accepted('admin', 'author')
def profile():
    posts = current_user.posts 
    return render_template('profile.html', posts=posts)

@main.route('/users')
@login_required
@roles_required('admin')
def users():
    users = User.query.all()
    return render_template('users.html', users = users)

@main.route('/delete_users/<int:user_id>')
@login_required
@roles_required('admin')
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if(user.email=='admin@example.com'):
        return redirect(url_for('main.users'))
    Post.query.filter_by(author=user).delete()
    User.query.filter_by(id=user_id).delete()
    UserRoles.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    return redirect(url_for('main.users'))

@main.route('/blogs')
@login_required
@roles_required('admin')
def blogs():
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template('blogs.html', posts=posts)