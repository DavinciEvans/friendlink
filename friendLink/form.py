from wtforms import Form, StringField, PasswordField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8,20)])
    submit = SubmitField('Login')


class SettingsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(8,20)])
    submit = SubmitField("Submit")


class EditForm(FlaskForm):
    avatar = FileField('Avatar', validators=[FileAllowed(['jpg','jpeg','png','webp','gif'])])
    name = StringField('Name', validators=[DataRequired(), Length(1, 60)])
    motto = StringField('Motto', validators=[DataRequired(), Length(1, 60)])
    submit = SubmitField("Submit")