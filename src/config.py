from os import getenv


class Config:
    DB_URL = getenv('ASYNC_POSTGRES_DATABASE_URL', '')
    LOG_LEVEL = getenv('LOG_LEVEL', 'DEBUG')
