# Import required modules and classes
from flask import Blueprint, render_template
from flask_login import login_required, current_user
import os

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)


# View function for the home page
@views.route('/')
@login_required  # Requires the user to be logged in to access this view
def home():
    # Render the 'home.html' template with the current user and authentication status
    return render_template("home.html", user=current_user, authenticated=current_user.is_authenticated)


# View function for the admin settings page
@views.route('/admin')
@login_required  # Requires the user to be logged in to access this view
def admin():
    # List all files in the 'static/databases/' directory
    db_files = os.listdir('static/databases/')
    # Render the 'admin.html' template with the current user
    return render_template("admin.html", user=current_user, database_files=db_files)


# View function for the upload records page
@views.route('/uploadRecords')
@login_required  # Requires the user to be logged in to access this view
def uploadRecords():
    # List all files in the 'static/databases/' directory
    db_files = os.listdir('static/databases/')

    # Render the 'uploadRecords.html' template with the current user, database files, and a flag to hide the progress
    return render_template("uploadRecords.html", user=current_user, database_files=db_files)


# View function for single match analysis
@views.route('/singleMatchAnalysis')
@login_required  # Requires the user to be logged in to access this view
def singleMatchAnalysis():
    # List all files in the 'static/databases/' directory
    db_files = os.listdir('static/databases/')
    # Render the 'singleMatchAnalysis.html' template with the current user
    return render_template("singleMatchAnalysis.html", user=current_user, database_files=db_files)
