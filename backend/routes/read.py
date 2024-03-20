import json
from flask import Blueprint
from services.read import read_secret

read_blueprint = Blueprint("read", __name__)


@read_blueprint.get("/read")
def get_read():
    return json.dumps(read_secret()), 200
