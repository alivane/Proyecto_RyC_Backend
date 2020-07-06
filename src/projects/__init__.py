from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from projects.configs import Config


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def register_blueprints(app):
    from projects.endpoints.users import blueprint as users
    from projects.endpoints.status import blueprint as status

    app.register_blueprint(users)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    return app