from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from projects.configs import Config
import marshmallow

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()


def register_blueprints(app):
    from projects.endpoints.users import blueprint as users
    from projects.endpoints.status import blueprint as status

    app.register_blueprint(users)


def register_error_handler(app):
    @app.errorhanfler(marshmallow.execptions.ValidationError)
    def validataion_error_handler(e):
        return jsonify(validatetion_error.messages), 400


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    register_blueprints(app)

    return app