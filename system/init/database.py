from system.db.db_init import init_db
from app.config import database as database_config
# import sqlalchemy

def initialize_db(app):
  init_db(app)

def _get_config(env):
    return {
        'DEVELOPMENT': database_config.DevelopmentDBConfig,
        'STAGING': database_config.StagingDBConfig,
        'PRODUCTION': database_config.ProductionDBConfig,
    }.get(env, database_config.DevelopmentDBConfig)


# create database functionality
# def create_database(app, db_name):
#     config = _get_config(os.getenv('PYLOT_ENV', 'DEVELOPMENT'))
#     database_url = "mysql://" + str(config.DB_USERNAME) + ":" + str(config.DB_PASSWORD) + "@127.0.0.1:" + str(config.DB_PORT)
#     engine = sqlalchemy.create_engine(database_url)
#     engine.execute("CREATE DATABASE {}".format(db_name))
#     engine.execute("USE {}".format(db_name))
