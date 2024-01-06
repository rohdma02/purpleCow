from flask import Flask

from extensions import db
from routes import main


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://purplecow_user" + \
        ":gznjp07naYyT8PUZEIyqpS8F9n8VVcc2@dpg-cmc9v3ol5elc739f19u0-a." + \
        "oregon-postgres.render.com/purplecow"

    db.init_app(app)

    app.register_blueprint(main)

    return app
