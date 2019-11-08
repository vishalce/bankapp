from flask import Flask
from .config import app_config
from .models import bcrypt
from .models import db
from .views.user import user_api
from .views.bank import bank_api


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_api, url_prefix='/api/v1/users')
    app.register_blueprint(bank_api, url_prefix='/api/v1/banks')

    @app.route('/', methods=['GET'])
    def index():
        return 'Hello World'

    return app
