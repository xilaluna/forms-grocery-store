from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from grocery_app.config import Config
import os


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

bcrypt = Bcrypt(app)

from grocery_app.routes import main  # nopep8


app.register_blueprint(main)

with app.app_context():
    db.create_all()
