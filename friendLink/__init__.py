from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SERVER_NAME"] = "127.0.0.1:5000"
db = SQLAlchemy(app)

@app.route('/')
def index():
    friendList = [
        {
            'avatar': url_for('static', filename='avatar1.jpg'),
            'name': "蝉时雨",
            'motto': "蝉鸣如雨，花落道中",
            'link': "https://chanshiyu.com/"
        },
        {
            'avatar': url_for('static', filename='avatar2.jpg'),
            'name': "Mashiro",
            'motto': "提供主题的作者大大！",
            'link': "https://2heng.xin/"
        },
        {
            'avatar': url_for('static', filename='avatar3.jpg'),
            'name': "小透明・宸",
            'motto': " 存在感满满的好孩子(´•ω•`)",
            'link': "https://akarin.dev/"
        },
        {
            'avatar': url_for('static', filename='avatar4.jpg'),
            'name': "imByteCat",
            'motto': "身边某个dalao(๑•̀ㅂ•́)و✧",
            'link': "https://2forest.cn/"
        }
    ]
    return render_template('index.html',friendList=friendList)


if __name__ == '__main__':
    app.run()
