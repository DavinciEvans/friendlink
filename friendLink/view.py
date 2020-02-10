from friendLink import app, db
from friendLink.model import User, Friend
from flask import render_template, url_for, flash, redirect, send_from_directory
from friendLink.form import LoginForm, SettingsForm, EditForm
from flask_login import login_user, login_required, logout_user


@app.route('/')
def index():
    friendList = Friend.query.all()
    return render_template('index.html',friendList=friendList)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    user = User.query.first()
    if form.validate_on_submit(): # 判断是否正确提交表单
        username = form.username.data # data即为读取表单中的数据
        password = form.password.data
        if username == user.username and user.validate_password(password):
            login_user(user) # flask_login提供的登录函数
            flash("登录成功！")
            return redirect(url_for("index"))
        else:
            flash("用户名或密码错误")
            return redirect(url_for("login"))
    return render_template('login.html', form=form)


@app.route("/settings", methods=['POST', 'GET'])
@login_required
def settings():
    form = SettingsForm()
    if form.validate_on_submit():
        user = User.query.first()
        username = form.username.data
        password = form.password.data
        user.username = username
        user.password = user.set_password(password)
        db.session.commit()
        logout_user()
        login_user(user)
        flash("用户状态已更新！")
        return redirect(url_for("index"))
    return render_template("settings.html", form=form)


@app.route("/logout")
@login_required
def logout():
    flash("BYEBYE")
    logout_user()
    return redirect(url_for("index"))


@app.route("/edit/<int:id>", methods=['GET','POST'])
@login_required
def edit(id):
    import os
    def random_name(filename):
        import uuid
        ext = os.path.splitext(filename)[1]
        new_name = uuid.uuid4().hex + ext
        return new_name

    form = EditForm()
    friend = Friend.query.get_or_404(id)
    if form.validate_on_submit():
        avatar = form.avatar.data
        name = form.name.data
        motto = form.motto.data
        if avatar:
            filename = random_name(avatar.filename)
            avatar_path = os.path.join(app.config['UPLOAD_PATH'], filename)
            avatar.save(avatar_path)
            friend.avatar = url_for("get_file", filename=filename)
        friend.name = name
        friend.motto = motto
        db.session.commit()
        flash("数据已更新！")
        return redirect(url_for("index"))

    return render_template("edit.html", friend=friend, form=form)


@app.route("/delete/<int:id>",methods=['POST'])
@login_required
def delete(id):
    friend = Friend.query.get_or_404(id)
    db.session.delete(friend)
    db.session.commit()
    flash("已删除")
    return redirect(url_for("index"))


@app.route("/uploads/<path:filename>")
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)