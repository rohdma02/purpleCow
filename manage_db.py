from app import create_app
from extensions import db

app = create_app()


@app.cli.command()
def init_db():
    with app.app_context():
        # Check if tables exist before creating them
        existing_tables = db.engine.table_names()
        if not existing_tables:
            db.create_all()
            print("Database tables created.")
        else:
            print("Database tables already exist.")


if __name__ == "__main__":
    app.run()
