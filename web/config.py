import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gsolvit'#用于确保用户数据的安全性

    @staticmethod
    def init_app(app):
        pass

config = {
    'default': Config,
    'MYSQL_PASSWORD': '2002821',
    'DATABASE_NAME': 'marinesystem'
}