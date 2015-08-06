""" 
    System Initialization File

    Loads initializers for configurations, database, and routes and creates the flask application
"""
from flask import Flask
import os

from app.config import routes

from system.init.configuration import initialize_config
from system.init.database import initialize_db
from system.init.routes import initialize_routes

def initialize_app():
    instance_path = os.path.abspath(os.path.dirname(__file__) + '/../..')
    template_folder = os.path.join(instance_path, 'app/views')
    static_folder = os.path.join(instance_path, 'app/static')

    app = Flask('app', static_folder=static_folder, template_folder=template_folder, instance_path=instance_path)

    initialize_config(app)
    initialize_db(app)
    initialize_routes(app)

    return app
