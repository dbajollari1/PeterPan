from flask import Blueprint

bpCampaigns = Blueprint('campaigns', __name__)

from peterpan.campaigns import routes
