"""
    System Core Model File

    Core Model file that all Models inherit from

    Gives a model access to the db object
"""
from flask import current_app

class Model(object):
    def __init__(self):
        self.db = current_app.db
