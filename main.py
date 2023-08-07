# Import the 'create_app' function from the '__init__.py' file in the current directory
from . import create_app

# Call the 'create_app' function to create the Flask application instance
app = create_app()

# Check if the script is being executed as the main module
if __name__ == '__main__':
    # Run the Flask application
    app.run()
