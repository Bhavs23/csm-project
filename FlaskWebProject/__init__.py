import logging
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# ---------------------------------------------------
# App Initialization
# ---------------------------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# Azure Blob settings
app.config['BLOB_CONNECTION_STRING'] = os.environ.get("BLOB_CONNECTION_STRING")
app.config['BLOB_CONTAINER'] = os.environ.get("BLOB_CONTAINER")
app.config['BLOB_ACCOUNT'] = os.environ.get("BLOB_ACCOUNT")
app.config['BLOB_STORAGE_KEY'] = os.environ.get("BLOB_STORAGE_KEY")

# ---------------------------------------------------
# Logging
# ---------------------------------------------------
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

# ---------------------------------------------------
# Database
# ---------------------------------------------------
db = SQLAlchemy(app)

# ---------------------------------------------------
# Login Manager
# ---------------------------------------------------
login = LoginManager()
login.login_view = 'login'
login.init_app(app)

#  REQUIRED FIX: user_loader to prevent Azure crash
from FlaskWebProject.models import User

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------------------------------------------
# Session
# ---------------------------------------------------
Session(app)

# ---------------------------------------------------
# Import routes
# ---------------------------------------------------
from FlaskWebProject import views
