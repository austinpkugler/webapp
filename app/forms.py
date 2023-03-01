from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    StringField,
    IntegerField
)
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange
)


class LocationForm(FlaskForm):
    name = StringField('Name', validators=[Length(min=1, max=100)])
    city = StringField('City', validators=[DataRequired(), Length(min=1, max=50)])
    address = StringField('Street', validators=[DataRequired(), Length(min=1, max=200)])
    zip_code = IntegerField('Zip Code', validators=[DataRequired(), NumberRange(min=1, max=99950)])
    submit = SubmitField('Create')
