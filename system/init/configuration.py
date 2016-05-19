"""
    Configuration initialization file

    This file initializes all of the base configurations defined in the config.base file
"""
from app.config import base
import os

def _get_config(env):
    return {
        'DEVELOPMENT': base.DevelopmentConfig,
        'STAGING': base.StagingConfig,
        'PRODUCTION': base.ProductionConfig,
    }.get(env, base.DevelopmentConfig)

def initialize_config(app):
    # turned off sql_alchemy_track_modifications, unused and a memory consumer
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    env = os.getenv('PYLOT_ENV', 'DEVELOPMENT')
    app.config.from_object(_get_config(env))
