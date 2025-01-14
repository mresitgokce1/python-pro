from app import db
from datetime import datetime

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    score = db.Column(db.Integer)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def is_highest_score(self):
        highest_score = Score.query.filter_by(
            user_id=self.user_id,
            exam_id=self.exam_id
        ).order_by(Score.score.desc()).first()
        
        return highest_score and highest_score.id == self.id
    