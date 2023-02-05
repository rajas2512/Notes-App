#setting up flask application
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os 
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #initiialise our app
    app = Flask(__name__) #__name__ represents name of the file 
    #Secure the cookies in session data related to our website
    app.config['SECRET_KEY'] = 'Hello World' #"Hello World is a secret key"
    #Storing databse
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #Initialise db by giving the flask app
    db.init_app(app)

    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note

    with app.app_context():
        db.create_all() 
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    #If the user is not logged in which page to show
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
       return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')