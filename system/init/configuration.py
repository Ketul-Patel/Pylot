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
    env = os.getenv('PYRO_ENV', 'DEVELOPMENT')
    app.config.from_object(_get_config(env))
