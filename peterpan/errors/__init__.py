from flask import Blueprint

bp = Blueprint('errors', __name__)

from peterpan.errors import handlers
