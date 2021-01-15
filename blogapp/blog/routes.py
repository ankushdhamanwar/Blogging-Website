from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_user, logout_user, login_required, current_user
from flask_security import current_user, login_required, roles_required, roles_accepted
from flask_security.utils import hash_password
from blogapp import db, user_datastore
from blogapp.models import User, Role, Post

blog = Blueprint('blog', __name__)

@blog.route('/create', methods=['GET','POST'])
@login_required
@roles_accepted('admin', 'author')
def create_blog():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        content = request.form['content']

        blog = Post(title=title, subtitle=subtitle, content=content, user_id=current_user.id)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create.html')

@blog.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()
    date_posted = post.date_posted.strftime('%B %d, %Y')
    return render_template('post.html', post=post, date_posted=date_posted)

@blog.route('/delete/<int:blog_id>')
@login_required
@roles_accepted('admin', 'author')
def delete_blog(blog_id):
    Post.query.filter_by(id=blog_id).delete()
    db.session.commit()
    return redirect(url_for('main.profile'))

@blog.route('/deletebyadmin/<int:blog_id>')
@login_required
@roles_required('admin')
def delete_blog_by_admin(blog_id):
    Post.query.filter_by(id=blog_id).delete()
    db.session.commit()
    return redirect(url_for('main.blogs'))