from flask import render_template,request,redirect,url_for,flash, abort
from . import main
from .forms import PostForm, UpdateProfile
from app.models import User, Post, Role
from flask_login import login_required, current_user
from .. import db,photos
import os


@main.route('/')
@main.route('/home')
@login_required
def index():
    posts = Post.query.all()
    business = Post.query.filter_by(category = 'Pickuplines').all()
    finance= Post.query.filter_by(category = 'Motivation').all()
    relationships= Post.query.filter_by(category = 'Technology').all()
    wellbeing = Post.query.filter_by(category = 'Interview').all()
    
    return render_template('index.html', posts = posts,business=business, finance=finance, relationships=relationships, wellbeing=wellbeing)

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
    return render_template('pitch.html', title='New Post', form = form)

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
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
