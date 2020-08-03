class config(object):
    DEBUG = True
    TESTING = False
    DB_NAME = 'test_database'
    DB_COLLECTION = 'data'
    DB_URI = 'mongodb://localhost:27017/'
    APP_PORT = '8050'


class DevelopmentConfig(config):
    DEBUG = False
    TESTING = False
    DB_NAME = 'test_database'
    DB_COLLECTION = 'data'
    APP_PORT = '8085'


class TestingConfig(config):
    DEBUG = False
    TESTING = False
    DB_NAME = 'test_database'
    DB_COLLECTION = 'data'
    APP_PORT = '8087'


class ProductionConfig(config):
    DEBUG = False
    TESTING = False
    DB_NAME = 'test_database'
    DB_COLLECTION = 'data'
    APP_PORT = '8090'


class JenkinsDevelopmentConfig(config):
    DEBUG = True
    TESTING = False
    DB_NAME = 'test_database'
    DB_COLLECTION = 'data'
    APP_PORT = '8086'


class JenkinsTestingConfig(config):
    DEBUG = True
    TESTING = False
    DB_NAME = 'test_database'
    DB_COLLECTION = 'data'
    APP_PORT = '8088'
