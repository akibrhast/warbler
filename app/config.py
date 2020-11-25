import os

class Config(object):
    # Get DB_URI from environ variable (useful for production/testing) or,
    # if not set there, use development local db.
    try:
       SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    except KeyError as keyerr:
        print(f'Freindly Message: Please add a DATABASE_URL key in your envirnoment variable')
        raise
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.environ.get('SECRET_KEY', "it's a secret")
