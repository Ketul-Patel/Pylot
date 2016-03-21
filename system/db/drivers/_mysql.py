import mysql.connector
import collections
import inspect
import models
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

def _convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(_convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(_convert, data))
    else:
        return data



def connect(config, app):
    dbconfig = {
        'user': config.DB_USERNAME,
        'password': config.DB_PASSWORD,
        'database': config.DB_DATABASE_NAME,
        'host': config.DB_HOST,
        'port': config.DB_PORT,
    }
    dbconfig.update(config.DB_OPTIONS)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://" + str(config.DB_USERNAME) + ":" + str(config.DB_PASSWORD) + "@127.0.0.1:" + str(config.DB_PORT) + "/" + config.DB_DATABASE_NAME
    for name, obj in inspect.getmembers(models):
        if inspect.isclass(obj):
            setattr(app, name, obj)
    db = SQLAlchemy(app)

    def _query_db(query, data=None):
        result = db.session.execute(text(query), data)
        if query[0:6].lower() != 'select':
            app.db.session.commit()
            return True
        else:
            return result

    def _get_one(query, data=None):
        result = db.session.execute(text(query), data).fetchone()
        return result

    db.query_db = _query_db
    db.get_one = _get_one
    return db




