"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from system.init import initialize_app
from system.init.database import create_database
import subprocess
import os

app = initialize_app()

manager = Manager(app)

db = app.db

@manager.option('-db', '--database', help='database name')
def create_db(database):
	create_database(app, database)

 
migrate = Migrate(app, db)

manager.add_command('runserver', Server(host='127.0.0.1'))
manager.add_command('db', MigrateCommand)

"""
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  body = db.Column(db.Text)
 
  def __init__(self, title, body):
        self.title = title
        self.body = body
"""
if __name__ == "__main__":
    manager.run()
