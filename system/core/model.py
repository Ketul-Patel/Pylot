"""
    System Core Model File

    Core Model file that all Models inherit from

    Gives a model access to the db object
    
"""
from flask import current_app
from flask.ext.bcrypt import Bcrypt
import inspect

class Model(object):
    def __init__(self):
        self.db = current_app.db
        self.bcrypt = Bcrypt(current_app)