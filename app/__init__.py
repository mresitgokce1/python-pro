from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Bu sayfayı görüntülemek için lütfen giriş yapın.'

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app, db)
    
    from app.routes import auth_bp, teacher_bp, student_bp, main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(teacher_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(main_bp)

    return app
