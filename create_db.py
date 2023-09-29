from app import create_app

# Import your database models
from app.models import User

# Create a Flask app with the application context
app, db, bcrypt, login_manager = create_app()

with app.app_context():
    # Create the database tables
    db.create_all()
