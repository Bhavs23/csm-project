import os
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import app, db
from .models import User, Post
from .forms import LoginForm, CreateForm
import logging

logger = logging.getLogger("views")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", posts=posts)


# -----------------------------
# LOGIN
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("index"))

        flash("Invalid username or password")

    return render_template("login.html", form=form)


# -----------------------------
# LOGOUT
# -----------------------------
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


# -----------------------------
# CREATE ARTICLE
# -----------------------------
@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = CreateForm()

    if request.method == "POST" and form.validate_on_submit():
        file = request.files["image"]
        post = Post()
        post.save_changes(form, file, current_user.id, new=True)
        flash("Article created!")
        return redirect(url_for("index"))

    return render_template("create.html", form=form)


# -----------------------------
# VIEW ARTICLE
# -----------------------------
@app.route("/article/<int:id>")
def article(id):
    post = Post.query.get_or_404(id)
    return render_template("article.html", post=post)


# -----------------------------
# EDIT ARTICLE
# -----------------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    form = CreateForm(obj=post)

    if request.method == "POST" and form.validate_on_submit():
        file = request.files["image"]
        post.save_changes(form, file, current_user.id)
        flash("Article updated!")
        return redirect(url_for("article", id=post.id))

    return render_template("edit.html", form=form, post=post)


# -----------------------------
# DELETE ARTICLE
# -----------------------------
@app.route("/delete/<int:id>")
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash("Article deleted.")
    return redirect(url_for("index"))
