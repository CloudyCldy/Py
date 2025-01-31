from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

def init_db(app):
    """
    Initializes the database and binds the app to the SQLAlchemy instance.
    """
    db.init_app(app)  # Bind the app with the db instance
    with app.app_context():  # Ensure we are within the app context
        db.create_all()  # Create all tables if they don't exist
