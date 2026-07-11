from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    """Initialize SQLAlchemy with the Flask application."""
    db.init_app(app)