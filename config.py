import os


class Config(object):
    """Aplication config"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or ''

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or ''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
