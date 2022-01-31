import logging
import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'change-this-please'
    JWT_SECRET_KEY = 'another-key-to-change'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    TESTING = True


def get_env_config(ENV) -> Config:
    config = {
        'LOCAL': DevelopmentConfig,
        'TEST': TestingConfig
    }
    return config.get(ENV)


def get_logger_config() -> logging.Logger:
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(levelname)-6s :: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger
