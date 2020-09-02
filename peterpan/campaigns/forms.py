from wtforms import Form, StringField, TextAreaField, DateField, BooleanField, SelectField, HiddenField, SubmitField, validators, ValidationError
import datetime

class CampaignForm(Form):
    campaignTitle = StringField('Title', [validators.Length(min=4, max=100), validators.DataRequired()])
    campaignDate = DateField('Campaign Date', [validators.DataRequired('Please enter campaign date in mm/dd/yyyy format')], format='%m/%d/%Y', default=datetime.datetime.today().strftime('%m/%d/%Y'))
    campaignLocation = TextAreaField('Location', [validators.Length(min=1, max=100), validators.DataRequired()])
    campaignDesc = TextAreaField('Details', [validators.Length(min=1, max=1000), validators.DataRequired()])
    startTime = SelectField('From')
    endTime = SelectField('To')
    campaignID = HiddenField()
