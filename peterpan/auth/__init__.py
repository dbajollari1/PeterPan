from flask import Blueprint

bpAuth = Blueprint('auth', __name__)

from peterpan.auth import routes