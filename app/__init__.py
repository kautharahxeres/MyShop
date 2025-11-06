import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy (will be bound to app in factory)
db = SQLAlchemy()


def create_app(test_config=None):
    """Application factory. Returns a configured Flask app with SQLAlchemy."""
    app = Flask(__name__, instance_relative_config=True)

    # Basic config - store SQLite DB in the instance folder
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        SQLALCHEMY_DATABASE_URI=(
            os.environ.get('DATABASE_URL') or
            'sqlite:///' + os.path.join(app.instance_path, 'myshop.sqlite')
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is not None:
        app.config.update(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Initialize extensions
    db.init_app(app)

    # Register blueprints / routes
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
