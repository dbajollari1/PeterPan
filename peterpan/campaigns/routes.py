from flask import render_template, redirect, url_for, request, flash, redirect
from peterpan.campaigns import bpCampaigns
from peterpan.campaigns.models import Campaign
from peterpan.dataaccess.campaignsDAO import getCampaigns, saveCampaign, getCampaign, updateCampaign, deleteCampaign
from peterpan.campaigns.forms import CampaignForm
import datetime
from flask_login import login_required, current_user
from flask import current_app as app

@bpCampaigns.route('/campaigns')
def campaigns():
    """
    try:
        campaignList= getCampaigns()
        return render_template('campaigns/campaigns.html', campaignList = campaignList)
    except Exception as e:
        app.logger.error(str(e), extra={'user': ''})
        return redirect(url_for('errors.error'))
    """
    return render_template('campaigns/campaigns.html')

@bpCampaigns.route('/campaign', methods=('GET', 'POST'))
@login_required
def campaign(campaign_id = 0):
    
    if current_user.userRole != 'A':
        app.logger.error('Unauthorized!!!!', extra={'user': current_user.email})
        return redirect(url_for('errors.error'))
    
    form = CampaignForm(request.form)

    fromchoices=[]
    for x in range(6,12):
        fromchoices.append((str(x) + ":00 AM", str(x) + ":00 AM"))
        fromchoices.append((str(x) + ":30 AM", str(x) + ":30 AM"))      
    fromchoices.append(( "12:00 PM", "12:00 PM"))
    fromchoices.append(("12:30 PM", "12:30 PM"))
    for x in range(1,12):
        fromchoices.append((str(x) + ":00 PM", str(x) + ":00 PM"))
        fromchoices.append(( str(x) + ":30 PM", str(x) + ":30 PM"))
    form.startTime.choices = fromchoices
    form.endTime.choices = fromchoices

    if request.method == "GET":
        form.campaignID.data = campaign_id
        if int(form.campaignID.data) > 0:
            campaign = getCampaign(campaign_id)
            form.campaignTitle.data = campaign.campaignTitle
            form.campaignDate.data = campaign.campaignDate
            form.campaignLocation.data = campaign.campaignLocation
            form.campaignDesc.data = campaign.campaignDesc
            form.startTime.data = campaign.startTime
            form.endTime.data = campaign.endTime
        else:
            form.startTime.data="7:00 PM"
            form.endTime.data="9:00 PM"
            form.campaignDate.data = datetime.datetime.today().strftime('%m/%d/%Y')

    if request.method == "POST":
        if form.validate() == False:
            try:
                form.campaignDate.data = form.campaignDate.data.strftime('%m/%d/%Y')
            except:
                pass
            return render_template('campaigns/campaign.html',form = form) 
        #save to db
        try:
            campaign = Campaign(form.campaignID.data, form.campaignTitle.data, form.campaignLocation.data, form.campaignDesc.data, form.campaignDate.data, form.startTime.data, form.endTime.data)
            if int(form.campaignID.data) > 0:
                updateCampaign(campaign)
            else:
                saveCampaign(campaign)
            return redirect("/campaigns") #go to campaigns page
        except Exception as e:
            app.logger.error(str(e), extra={'user': ''})
            return redirect(url_for('errors.error'))
    
    return render_template('campaigns/campaign.html',form = form)

@bpCampaigns.route('/removeCampaign/<campaign_id>')
@login_required
def removeCampaign(campaign_id = 0):
    try: 
        if current_user.userRole != 'A':
            app.logger.error('Unauthorized!!!!', extra={'user': current_user.email})
            return redirect(url_for('errors.error'))
        deleteCampaign(campaign_id)
        return redirect("/campaigns") #reload page
    except Exception as e:
        app.logger.error(str(e), extra={'user': ''})
        return redirect(url_for('errors.error'))
