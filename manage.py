"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.migrate import Migrate, MigrateCommand
from system.init import initialize_app
# from system.init.database import create_database
import subprocess
import os

app = initialize_app()

manager = Manager(app)

# implement later, just creates database, needs to have mysql server installed 
# @manager.option('-db', '--database', help='database name')
# def create_db(database):
#   create_database(app, database)

manager.add_command('runserver', Server(host='127.0.0.1'))

if __name__ == "__main__":
    manager.run()
