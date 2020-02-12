import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.context_processor  # 该函数可以用于设置一个全局变量，里面的东西会在任意模板中生效
def inject_user():  # 函数名可以随意修改
    from friendLink.model import User
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于return {'user': user}


@login_manager.user_loader  # loginManager需要一个这个实例化方法
def load_user(user_id):  # 用户加载回调函数
    from friendLink.model import User
    user = User.query.get(int(user_id))
    return user


WIN = sys.platform.startswith('win')  # 检测是否为windows
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控，提高性能，官方推荐关闭
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # 文件的最大大小
app.config['UPLOAD_PATH'] = os.path.join(app.static_folder, 'uploads')

# 注册日志
import logging
from logging.handlers import RotatingFileHandler


def register_logger():
    app.logger.setLievel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = RotatingFileHandler('Logs/friendlink.log', maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    if not app.debug:
        app.logger.addHandler(file_handler)


from friendLink import command, view, form
if __name__ == '__main__':
    app.run()
