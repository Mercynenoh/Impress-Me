from flask import render_template,request,redirect,url_for,flash, abort
from . import main
from .forms import PostForm, UpdateProfile, CommentForm
from app.models import User, Post, Role, Comment
from flask_login import login_required, current_user
from .. import db,photos
import os


@main.route('/')
@main.route('/home')
@login_required
def index():
    posts = Post.query.all()
    comments = Comment.query.all()
    user = User.query.all()
    
    return render_template('index.html', posts = posts, comments=comments)

@main.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(category=form.category.data, pitch=form.pitch.data, author= current_user)
        flash('Your pitch has been created')
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('pitch.html', title='New Pitch',
    form = form, legend='New Pitch')

@main.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', category=post.category, post=post)

@main.route("/post/<int:post_id>/update",  methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.category = form.category.data
        post.pitch = form.pitch.data
        db.session.commit()
        return redirect(url_for('main.post', post_id=post.id))
    elif request.method == 'GET':
        form.category.data = post.category
        form.pitch.data = post.pitch
    return render_template('pitch.html', title = 'Update pitch', form = form,
    legend='Update Pitch')

@main.route('/post/<int:post_id>/comment',methods= ['GET', 'POST'])
@login_required
def comment(post_id):
    post = Post.query.get_or_404(post_id)
    comment = Comment.query.get(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.text.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('comment.html', title='New Comment', form = form)

@main.route("/post/<int:post_id>/delete",  methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted.', 'success')
    return redirect(url_for('main.index'))





@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'static/photos' in request.files:
        filename = photos.save(request.files['static/photos'])
        path = f'static/photos{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



