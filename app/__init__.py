from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


# Define the create_app function to create the Flask app instance
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)
    login_manager.login_view = "login"

    return app, db, bcrypt, login_manager


# Import the app and other modules after defining create_app
app, db, bcrypt, login_manager = create_app()

from app import routes
