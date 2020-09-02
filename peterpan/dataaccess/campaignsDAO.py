from peterpan.dataaccess.db_helper import execute_sql
from peterpan.campaigns.models import Campaign
import datetime

def getCampaigns():
    campaignList=[]
    campaigns = execute_sql(
        "SELECT campaign.id, campaign.title, campaign.description, campaign.location, campaign.campaignDate, campaign.startTime, campaign.endTime FROM campaign WHERE campaignDate >= date('now') ORDER BY campaignDate")

    for row in campaigns:
        campaign = Campaign()
        campaign.campaignId = row['id']
        campaign.campaignTitle = row['title']
        campaign.campaignDesc = row['description'].split('\n') #.replace("\n", "<br/>")
        campaign.campaignLocation = row['location']
        campaign.campaignDate = datetime.datetime.strptime(row['campaigndate'],'%Y-%m-%d').strftime('%d-%b-%Y')
        campaign.startTime = row['startTime']
        campaign.endTime = row['endTime']
        campaignList.append(campaign)
        
    return campaignList


def getCampaign(campaign_id):
    sql = 'SELECT * from campaign where id = ?'
    row = execute_sql (sql, (campaign_id,), False, True)
    campaign = Campaign()
    campaign.campaignTitle = row['title']
    campaign.campaignDesc = row['description']
    campaign.campaignLocation = row['location']
    campaign.campaignDate = datetime.datetime.strptime(row['campaigndate'],'%Y-%m-%d').strftime('%m/%d/%Y')
    campaign.startTime = row['startTime']
    campaign.endTime = row['endTime']
    return campaign

def saveCampaign(campaign): 
    sql = 'INSERT into campaign (title, description, location, campaignDate, startTime, endTime, status, createdBy, createdOn) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
    execute_sql (sql, (campaign.campaignTitle, campaign.campaignDesc, campaign.campaignLocation, 
    campaign.campaignDate, campaign.startTime, campaign.endTime, 'A', 'David',datetime.datetime.utcnow()), True)

def deleteCampaign(campaign_id):
    sql = 'DELETE from campaign where id = ?'
    execute_sql (sql, (campaign_id,), True, False)

def updateCampaign(campaign):
    sql = 'UPDATE campaign set title = ? , description = ?, location = ? , campaignDate = ?, startTime = ?, endTime = ?, status = ? , createdBy = ?, createdOn = ? WHERE id = ?'
    execute_sql(sql, (campaign.campaignTitle, campaign.campaignDesc, campaign.campaignLocation, 
    campaign.campaignDate, campaign.startTime, campaign.endTime, 'A', 'David',datetime.datetime.utcnow(), campaign.campaignId),  True)

