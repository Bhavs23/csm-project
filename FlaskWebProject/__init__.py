import logging
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Load Azure Blob config
app.config['BLOB_CONNECTION_STRING'] = os.environ.get("BLOB_CONNECTION_STRING")
app.config['BLOB_CONTAINER'] = os.environ.get("BLOB_CONTAINER")
app.config['BLOB_ACCOUNT'] = os.environ.get("BLOB_ACCOUNT")
app.config['BLOB_STORAGE_KEY'] = os.environ.get("BLOB_STORAGE_KEY")

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
console.setFormatter(formatter)
app.logger.addHandler(console)

app.logger.info("Flask app initialized and logging configured.")

Session(app)
db = SQLAlchemy(app)

# FIXED LOGIN MANAGER
login = LoginManager()
login.login_view = 'login'
login.init_app(app)

# Import routes
import FlaskWebProject.views
