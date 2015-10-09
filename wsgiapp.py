"""WSGI app to run the cleansweep application in production.

The config file can be specified using environment variable CLEANSWEEP_CONFIG.
If not specified, it defaults to config/production.cfg.

USAGE:

    gunicorn wsgiapp:app

    CLEANSWEEP_CONFIG=config/production_xyz.cfg gunicorn wsgiapp:app
"""
import os
from cleansweep.main import init_app

config_file = os.environ.get("CLEANSWEEP_CONFIG", "config/production.cfg")
app = init_app(config_file)
