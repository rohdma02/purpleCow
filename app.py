import os
from flask import render_template
from . import create_app, db
from .models import Cow, Feeding, Medication, Weight, Reproduction, Show, Note
from dotenv import load_dotenv

load_dotenv()

app = create_app(os.getenv("CONFIG_MODE"))


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/animals/")
def animals():
    return render_template("animals.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # This will create the tables
    app.run()
