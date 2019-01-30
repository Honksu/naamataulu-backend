import os

def getEnvironmentVariable(type=str, key=None, default=''):
    try:
        return type(os.environ[key])
    except KeyError:
        return type(default)