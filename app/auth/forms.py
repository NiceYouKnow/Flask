from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')
# 登录模板


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='密码不一致')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_email(self, filed):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('邮箱已注册！')

    def validate_username(self, filed):
        if User.query.filter_by(username=filed.data).first():
            raise ValidationError('该用户名已存在！')
# 注册模版


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('password2', message='密码不一致！')])
    password2 = PasswordField('Confirm New Password', validators=[DataRequired()])
    submit = SubmitField('修改密码')

# 修改密码模板


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('重置密码')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('password2', message='密码不一致！')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('重置密码')

# 重置密码


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('更换邮箱')

    def validata_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('邮箱已被注册！')
# 修改邮箱
