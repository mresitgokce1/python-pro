from app import db
from datetime import datetime
from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE = 'multiple_choice'
    TEXT = 'text'

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'))
    interest = db.relationship('Interest', backref='exams')
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref='exam', lazy=True)
    scores = db.relationship('Score', backref='exam', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    question_text = db.Column(db.String(500), nullable=False)
    question_type = db.Column(db.Enum(QuestionType), nullable=False)
    correct_answer = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(500))
    student_answers = db.relationship('StudentAnswer', backref='question', lazy=True)
    