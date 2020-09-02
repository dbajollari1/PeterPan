from flask import render_template, redirect, url_for, request, flash, redirect
from peterpan.public import bp
from peterpan.public.forms import ContactForm
from peterpan.services.mail_api import send_email
from flask import current_app as app


@bp.route('/about')
def about():
    return render_template('public/whatwedo.html')

    
@bp.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm(request.form)
    if request.method == "POST":
        if form.validate() == False:    
            return render_template('public/contact.html',form = form)
            
        inputMessage = form.inputMessage.data
        inputName = form.inputName.data
        inputEmail = form.inputEmail.data

        send_email('Fort Lee Artist Guild - Contact Request', app.config['ADMINS'],
        'Name: ' + inputName + '\n' + 'Email: ' + inputEmail +  '\n\n' + 'Message: ' + inputMessage, '')

        flash("Thank You. Your request has been received. We will respond to you as soon as possible.")
        return redirect("/") #go to home page

    return render_template('public/contact.html',form = form)


