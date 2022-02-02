
class Config:
    API_KEY = "742cd48b060a4caeab75d9734d1a78e5"
    SECRET_KEY=1234567


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}