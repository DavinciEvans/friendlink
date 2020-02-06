from friendLink import app, db
from friendLink.model import User, Friend
from flask import render_template, url_for
from friendLink.form import LoginForm

@app.route('/')
def index():
    friendList = Friend.query.all()
    return render_template('index.html',friendList=friendList)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)