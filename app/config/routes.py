"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import route

# TODO: Move initialization method to init folder and create a more "User Friendly" system for defining routes (see codeigniter routes)
def initialize_routes(app):
    from app.controllers.WelcomeController import WelcomeController
    route(app, 'index', '/', WelcomeController, 'index')
