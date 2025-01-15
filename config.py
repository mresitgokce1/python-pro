import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    if os.environ.get('PYTHONANYWHERE_DOMAIN'):
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mrgokce:Dsa13542o1o!@mrgokce.mysql.pythonanywhere-services.com/mrgokce$default'
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///exam_system.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
