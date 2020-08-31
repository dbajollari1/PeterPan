from flask import Flask, render_template, request, redirect, url_for, flash, session, redirect   
from peterpan import create_app, db
from peterpan.dataaccess.homeDAO import getUpcomingEvent
from peterpan.events.models import Event
from peterpan.services.mail_api import send_email


app = create_app()

@app.route('/')
@app.route('/home')
def home():
    try:
        # event = getUpcomingEvent()
        return render_template('index.html') #, event = event)
    except Exception as e:
        app.logger.error(str(e), extra={'user': ''})
        return redirect(url_for('errors.error', msg=str(e)))




    



