from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import login_user
from .models import User, Song
from . import db, login_manager


main_dp = Blueprint('main', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


class UserView:
    def __init__(self):
        pass
        
    @main_dp.route('/login', methods=["GET", "POST"])
    def login(self):
        login = request.form.get('login')
        password = request.form.get('password')

        if login and password:
            user = User.query.get(login)
            if not user:
                pass
            if password == '2007':
                login_user(user)

                next_page = request.args.get('next')
                redirect(next_page)
            else:
                return flash('Invalid credentials!')
        else:
            return render_template("users/login.html")


    @main_dp.route('/register', methods=["GET", "POST"])
    def register(self):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email = request.form.get("email")
        avatar = request.form.get("avatar")

        if password1 == password2:
            print("Yes")

    @main_dp.route("/logout", methods=["GET", "POST"])
    def logout(self):
        pass


@main_dp.route('/')
def index():
    context = {}
    users = Song.query.all()
    
    context['users'] = users

    return render_template("index.html", **context)


@main_dp.route('/about')
def about():
    return render_template("about.html")


@main_dp.route("/songs")
def songs():
    return render_template("songs.html")


@main_dp.route("/categories")
def categories():
    return render_template("categories.html")