from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app.models.interest import Interest

user_interests = db.Table('user_interests',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('interest_id', db.Integer, db.ForeignKey('interest.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_teacher = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    interests = db.relationship('Interest', 
                              secondary=user_interests,
                              backref=db.backref('users', lazy='dynamic'))
    
    created_interests = db.relationship('Interest', 
                                      backref='creator', 
                                      foreign_keys=[Interest.created_by])
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
