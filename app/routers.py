from flask import Blueprint, render_template, redirect
from .models import User, Song
from . import db

main_dp = Blueprint('main', __name__)


@main_dp.route('/')
def index():
    context = {}
    users = Song.query.all()
    
    context['users'] = users

    return render_template("index.html", **context)


@main_dp.route('/about')
def about():
    return render_template("about.html")