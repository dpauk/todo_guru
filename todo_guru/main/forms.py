from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField
from wtforms.validators import Required, Length


class TodoEntryForm(FlaskForm):
    name = StringField('Todo name', validators=[Required(), Length(1, 250)])
    notes = TextAreaField('Notes', validators=[Length(0, 1000)])
    due_on = DateField('Due date', format='%Y-%m-%d')

    submit = SubmitField('Add todo')
