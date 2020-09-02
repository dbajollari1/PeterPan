from flask import Flask, render_template, request, redirect, url_for, flash, session, redirect   
from peterpan import create_app, db
from peterpan.dataaccess.homeDAO import getUpcomingCampaign
from peterpan.campaigns.models import Campaign
from peterpan.services.mail_api import send_email


app = create_app()

@app.route('/')
@app.route('/home')
def home():
    try:
        # campaign = getUpcomingCampaign()
        return render_template('index.html') #, campaign = campaign)
    except Exception as e:
        app.logger.error(str(e), extra={'user': ''})
        return redirect(url_for('errors.error', msg=str(e)))




    



