from flask import Blueprint

bpEvents = Blueprint('events', __name__)

from peterpan.events import routes
