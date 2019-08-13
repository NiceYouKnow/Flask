from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, \
    BooleanField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email
from ..models import Role, User
from flask_pagedown.fields import PageDownField

class NameForm(FlaskForm):
    name = StringField('你的名字是？', validators=[DataRequired()])
    # date = DateField("Date", default=datetime.now())
    password = PasswordField('你的密码是？')
    submit = SubmitField('提交')  # 表单类


class EditProfileForm(FlaskForm):
    name = StringField('姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 64)])
    confirmed = BooleanField('验证')
    role = SelectField('Role', coerce=int)
    name = StringField('姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [
            (role.id, role.name)
            for role in Role.query.order_by(Role.name).all()
        ]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册！')

    def validate_username(self, field):
        if field.data != self.user.username and \
               User.query.filter_by(username=field.data).first():
            raise ValidationError('Username已被占用!')


class PostForm(FlaskForm):
    body = PageDownField('你有什么想说的？', validators=[DataRequired(0)])
    submit = SubmitField('提交')


class CommentForm(FlaskForm):
    body = StringField('输入您的评论', validators=[DataRequired()])
    submit = SubmitField('提交')
