from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8,20)])
    submit = SubmitField('Login')