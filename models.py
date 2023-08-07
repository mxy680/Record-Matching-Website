# Import the 'db' instance, which is an instance of SQLAlchemy
from . import db
from flask_login import UserMixin


# Define the User model class, which represents a table in the database
class User(db.Model, UserMixin):
    # Define the columns of the User table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column, auto-incremented integer
    email = db.Column(db.String(150), unique=True)  # Email column, unique constraint
    password = db.Column(db.String(100))  # Password column
    isAdmin = db.Column(db.Boolean, default=False)  # isAdmin column, defaults to False
