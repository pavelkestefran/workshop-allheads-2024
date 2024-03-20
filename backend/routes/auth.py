import json
from flask import Blueprint
from services.auth import is_authenticated

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.get("/auth-status")
def get_auth_status():
    return json.dumps(is_authenticated()), 200
