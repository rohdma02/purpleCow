import os


class Config(object):
    """Aplication config"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'zaring'

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'postgresql://purplecow_user:gznjp07naYyT8PUZEIyqpS8F9n8VVcc2@dpg-cmc9v3ol5elc739f19u0-a.oregon-postgres.render.com/purplecow'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

# In change of DB configuration of tables and columns follow the procedure:
# On windows type the following command to make database changes
#
# "ACTIVATE YOUR VIRTUAL ENVIRONMENT"
# set FLASK_APP=main.py
# set FLASK_ENV=development
# flask db init
# flask db migrate -m "TYPE WHAT YOU CHANGED HERE"
# flask db upgrade
#
# Connect to DB and check for changes!
