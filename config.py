import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '97CU8jSU5d2a9eyNopZi3O7LNtGteeFB'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///exam_system.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
