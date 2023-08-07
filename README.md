# Record-Matching-Website

Record Matching Web Application

This is a web application built with Flask and Python that allows users to perform record matching and analysis on datasets. Users can upload their datasets, and the application uses the rapidfuzz library to find the closest matches in a separate database. The application supports single-match analysis and can display the closest matches to a user-inputted record name. Admin users have additional functionalities, such as uploading and updating databases, as well as deleting databases.

Features:
- User authentication and authorization with login and sign-up functionality.
- Record matching using the rapidfuzz library with customizable match threshold.
- Single-match analysis to find the closest matches to a user-inputted record name.
- Admin user functionality to upload, update, and delete databases.
- User-friendly web interface using Bootstrap and Jinja2 templating.

Technologies used:
- Flask: Python web framework for building the web application.
- SQLAlchemy: ORM library to interact with the database.
- rapidfuzz: Python library for fast fuzzy string matching.
- Pandas: Python data manipulation library for processing datasets.
- Bootstrap: Front-end framework for responsive and attractive design.
- Jinja2: Templating engine for rendering dynamic content.

Deployment:
The web application can be deployed on any web server that supports Python and Flask. It uses SQLite as the database for simplicity, but it can be easily adapted to other databases. The application can be deployed on a local server or on cloud platforms like Heroku or AWS.

Note:
Please ensure that you have Python and the required libraries installed before running the application. To set up the virtual environment and install the dependencies, use the requirements.txt file provided.

Feel free to contribute, report issues, or suggest improvements.
