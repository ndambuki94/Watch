from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting up Configuraton
app.config.from_object(DevConfig)

from app import views
