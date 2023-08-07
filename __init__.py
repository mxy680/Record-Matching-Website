# Import required modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

# Name of the database file
DB_NAME = "database.db"


def create_app():
    # Create a Flask application
    app = Flask(__name__)

    # Set a secret key for the application (for security purposes)
    app.config['SECRET_KEY'] = 'my_super_secret_key'

    # Configure the database URI for SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize the database with the app context
    db.init_app(app)

    # Import views and authentication blueprints
    from .views import views
    from .auth import auth

    # Register the blueprints with the app, assigning a URL prefix to each
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import the User model
    from .models import User

    # Create the database if it does not exist
    create_database(app)

    # Initialize the LoginManager
    login_manager = LoginManager()

    # Set the login view for the LoginManager (redirects to 'auth.login' if a login-required view is accessed)
    login_manager.login_view = 'auth.login'

    # Initialize the LoginManager with the app
    login_manager.init_app(app)

    # Define a user_loader function for the LoginManager to load a user by its ID
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Return the app instance
    return app


def create_database(app):
    # Check if the database file exists in the 'website' directory
    if not path.exists('website/' + DB_NAME):
        # If the database does not exist, create it along with the tables defined in the models
        db.create_all(app=app)
        print('Created Database!')
