from flask import Blueprint

bp = Blueprint('public', __name__)

from peterpan.public import routes
