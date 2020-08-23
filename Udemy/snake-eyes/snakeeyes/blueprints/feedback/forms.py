from flask_wtf import Form
from wtforms import RadioField, TextAreaField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Optional, Length


class FeedbackForm(Form):
    experience_choices = [
        ('good', 'Good'), 
        ('neutral', 'Neutral'), 
        ('bad', 'Bad')
    ]
    email = EmailField("What's your email address?",
                       [DataRequired(), Length(3, 254)])
    overall_experience = RadioField('Overall Experience', 
                                    choices=experience_choices,
                                    validators=[DataRequired()])
    playing_experience = RadioField('Playing Experience',
                                    choices=experience_choices,
                                    validators=[DataRequired()])
    account_experience = RadioField('Account Experience',
                                    choices=experience_choices,
                                    validators=[DataRequired()])
    concerns = TextAreaField('Any concerns?', [Optional(), Length(0, 8192)])
