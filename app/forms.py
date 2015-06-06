from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])

class AddNewFact(Form):
    fact = StringField('fact', widget=TextArea(), validators=[DataRequired()])
