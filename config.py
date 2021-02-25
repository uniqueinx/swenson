import os


class Config(object):
    DB = os.environ.get("DB")
