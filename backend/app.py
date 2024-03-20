import json
import logging
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS, cross_origin

from routes.auth import auth_blueprint
from routes.read import read_blueprint

# Configure with .env file
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


logger = logging.getLogger(__name__)

# Initialize Flask application
logger.debug("Creating the flask application")
app = Flask(__name__)

# Configure cross origin resource sharing (CORS)
CORS(app, origins=["http://localhost:4200"])

# Register the routes via blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(read_blueprint)

@app.route('/')
def index():
    return json.dumps("Hello, World"), 200

if __name__ == "__main__":
    # Run app in debug mode
    app.run(debug=True)
