"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from system.init import initialize_app
import subprocess

manager = Manager(initialize_app())

manager.add_command('runserver', Server(host='127.0.0.1'))

if __name__ == "__main__":
    manager.run()
