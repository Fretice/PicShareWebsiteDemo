from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import Required, Length, Email, EqualTo


class LoginForm(Form):
    email = StringField('邮箱', validators=[Required(),
                        Length(1, 60), Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我,下次直接登录')
    submit = SubmitField('登录')


class RegisterForm(Form):
    email = StringField('邮箱', validators=[Required(),
                        Length(1, 60), Email()])
    username = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    password2 = PasswordField('重复密码', validators=[Required(),
                              EqualTo('password', message='两次密码不一致.')])
    submit = SubmitField('注册')
