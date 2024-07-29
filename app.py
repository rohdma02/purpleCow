import os

from flask import render_template

# App Initialization
from . import create_app  # from __init__ file
app = create_app(os.getenv("CONFIG_MODE"))

# Hello World!


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/animals/")
def animals():
    return render_template("animals.html")


if __name__ == "__main__":
    app.run()
