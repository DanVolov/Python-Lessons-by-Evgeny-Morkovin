from flask import Flask
from config import Config
from уроки.январь.flask_shop.shop.extensions import db, login_manager, bcrypt, migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app