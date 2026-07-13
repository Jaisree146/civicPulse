from flask import Flask
from flask_migrate import Migrate
from config.db import db
from config.settings import Settings
from handlers.error_handler import register_error_handlers
from routes.auth_routes import auth_bp
from routes.complaint_routes import complaint_bp
from routes.issue_routes import issue_bp
from models.department import Department
from models.user import User
from models.role import Role
from models.category import Category
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Settings)

    db.init_app(app)

    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(complaint_bp)
    app.register_blueprint(issue_bp)
    register_error_handlers(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=Settings.DEBUG
    )