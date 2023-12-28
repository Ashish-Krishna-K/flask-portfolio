from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    """A class to handle the contact form"""

    name = StringField(label="Your Name", validators=[DataRequired()])
    company = StringField(label="Your Company Name(optional)")
    email = EmailField(
        label="Email", validators=[DataRequired(), Email()]
    )
    message = TextAreaField(label="Message(optional)")
    submit = SubmitField(label="Submit")
