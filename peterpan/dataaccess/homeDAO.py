from peterpan.dataaccess.db_helper import execute_sql
from peterpan.campaigns.models import Campaign
import datetime

def getUpcomingCampaign():
    sql = "SELECT * from campaign where campaignDate >= date('now') Order by campaignDate LIMIT 1"
    row = execute_sql (sql,(), False, True)
    if not row == None:
        campaign = Campaign()
        campaign.campaignTitle = row['title']
        campaign.campaignDesc = row['description']
        campaign.campaignLocation = row['location']
        campaign.campaignDate = datetime.datetime.strptime(row['campaigndate'],'%Y-%m-%d').strftime('%m/%d/%Y')
        campaign.startTime = row['startTime']
        campaign.endTime = row['endTime']
        return campaign
