import collections
import inspect
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
    # dbconfig.update(config.DB_OPTIONS)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://" + str(config.DB_USERNAME) + ":" + str(config.DB_PASSWORD) + "@127.0.0.1:" + str(config.DB_PORT) + "/" + config.DB_DATABASE_NAME
    db = SQLAlchemy(app)

    def _query_db(query, data=None):
        result = db.session.execute(text(query), data)
        if query[0:6].lower() == 'select':
            # if the query was a select
            # convert the result to a list of dictionaries
            list_result = [dict(r) for r in result]
            # return the results as a list of dictionaries
            return list_result
        elif query[0:6].lower() == 'insert':
            # if the query was an insert, return the id of the
            # commit changes
            app.db.session.commit()
            # row that was inserted
            return result.lastrowid
        else:
            # if the query was an update or delete, return nothing and commit changes
            app.db.session.commit()

    def _get_one(query, data=None):
        result = db.session.execute(text(query), data).fetchone()
        return result

    db.query_db = _query_db
    db.get_one = _get_one
    return db
