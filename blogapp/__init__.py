from flask import Flask
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "this is not a safe key please dont use this key in production environment"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['USER_ENABLE_EMAIL'] = False
    app.config['SECURITY_PASSWORD_SALT'] = 'secretsalt'
    db.init_app(app)

    
    security = Security(app, user_datastore)
    
    #user_manager.init_app(app)

    from .auth.routes import auth
    app.register_blueprint(auth)

    from .main.routes import main
    app.register_blueprint(main)
    return app