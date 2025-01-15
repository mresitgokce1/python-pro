import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '97CU8jSU5d2a9eyNopZi3O7LNtGteeFB'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') if os.environ.get('PYTHONANYWHERE_DOMAIN') else 'sqlite:///exam_system.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
