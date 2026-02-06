import os


class Config:
    SECRET_KEY = 'asfiojaklfjasklfjas'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


