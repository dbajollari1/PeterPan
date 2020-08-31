import os

class Config(object):
    SECRET_KEY = 'vfr'
    ADMINS = 'dbajollari1@yahoo.com'
    MJ_APIKEY_PUBLIC = '077fc21857d31f1f416fbf1ab7477164'
    MJ_APIKEY_PRIVATE = '03caddedf8edb44156d03585242e359a'
    MJ_EMAIL = 'arianb1@hotmail.com'
    SQLITE_PATH = 'db/flag.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/flag.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SUPPORT = 'arianb1@hotmail.com'