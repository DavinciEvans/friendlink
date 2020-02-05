from friendLink import app, db
from friendLink.model import User, Friend
from flask import render_template

@app.route('/')
def index():
    friendList = Friend.query.all()
    return render_template('index.html',friendList=friendList)