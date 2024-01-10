import os
from flask import Flask
from extensions import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://purplecow_user" + \
        ":gznjp07naYyT8PUZEIyqpS8F9n8VVcc2@dpg-cmc9v3ol5elc739f19u0-a." + \
        "oregon-postgres.render.com/purplecow" or os.environ.get(
            "DATABASE_URL")

    db.init_app(app)

    return app
