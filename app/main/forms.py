from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):

    category = SelectField('Pitch Category', choices=[('Pickuplines','Pickuplines'),('Motivation','Motivation'),('Technology','Technology'),('Interview','Interview')],validators=[DataRequired()])
    pitch = TextAreaField('Pitch',validators=[DataRequired()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
