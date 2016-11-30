import os

_basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    WEBSITE_PIC_PER_PAGE = 20  # how many pics in a page
    WEBSITE_FOLLOWERS_PER_PAGE = 50  # how many followers in a page
    WEBSITE_COMMENTS_PER_PAGE = 30  # how many comments in a page

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig:
    DEBUG = True
