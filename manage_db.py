from app import create_app
from extensions import db

app = create_app()


@app.cli.command()
def init_db():
    with app.app_context():
        db.create_all()
