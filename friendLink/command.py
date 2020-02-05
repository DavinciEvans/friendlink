import click
from friendLink import app, db
from friendLink.model import User,Friend

@app.cli.command()
@click.option('--drop', is_flag=True, help="Create after drop")
def initdb(drop):  # 数据库初始化
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initial database successful!")


@app.cli.command()
def forge():
    db.create_all()
    friendList = [
        {
            'avatar': "/static/avatar1.jpg",
            'name': "蝉时雨",
            'motto': "蝉鸣如雨，花落道中",
            'link': "https://chanshiyu.com/"
        },
        {
            'avatar': "/static/avatar2.jpg",
            'name': "Mashiro",
            'motto': "提供主题的作者大大！",
            'link': "https://2heng.xin/"
        },
        {
            'avatar': "/static/avatar3.jpg",
            'name': "小透明・宸",
            'motto': " 存在感满满的好孩子(´•ω•`)",
            'link': "https://akarin.dev/"
        },
        {
            'avatar': "/static/avatar4.jpg",
            'name': "imByteCat",
            'motto': "身边某个dalao(๑•̀ㅂ•́)و✧",
            'link': "https://2forest.cn/"
        }
    ]
    for f in friendList:
        fri = Friend(name=f["name"],avatar=f["avatar"],motto=f["motto"],link=f["link"])
        db.session.add(fri)
    db.session.commit()
    click.echo('Done.')

