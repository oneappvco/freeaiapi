import sys

# add your project directory to the sys.path
project_home = '/home/backupap/advancedai'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from adv import app as application  # noqa
