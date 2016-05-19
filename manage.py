"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from flask.ext.sqlalchemy import SQLAlchemy
from system.init import initialize_app

app = initialize_app()

manager = Manager(app)

manager.add_command('runserver', Server(host='127.0.0.1'))

if __name__ == "__main__":
    manager.run()
