from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Exam, Score, StudentAnswer, Interest
from app import db

bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_teacher:
        return redirect(url_for('teacher.dashboard'))
    
    all_interests = Interest.query.all()
    student_interests = current_user.interests
    exams = Exam.query.filter(Exam.interest_id.in_([i.id for i in student_interests])).all()
    return render_template('student/dashboard.html', 
                         exams=exams, 
                         all_interests=all_interests)

@bp.route('/update_interests', methods=['POST'])
@login_required
def update_interests():
    if current_user.is_teacher:
        return redirect(url_for('teacher.dashboard'))
    
    interest_ids = request.form.getlist('interests[]')
    selected_interests = Interest.query.filter(Interest.id.in_(interest_ids)).all()
    current_user.interests = selected_interests
    db.session.commit()
    flash('İlgi alanlarınız güncellendi.')
    return redirect(url_for('student.dashboard'))

@bp.route('/exam/<int:exam_id>')
@login_required
def take_exam(exam_id):
    if current_user.is_teacher:
        return redirect(url_for('teacher.dashboard'))
    
    exam = Exam.query.get_or_404(exam_id)
    highest_score = Score.query.filter_by(
        user_id=current_user.id,
        exam_id=exam_id
    ).order_by(Score.score.desc()).first()
    
    return render_template('student/take_exam.html', 
                         exam=exam, 
                         highest_score=highest_score)

@bp.route('/exam/<int:exam_id>/submit', methods=['POST'])
@login_required
def submit_exam(exam_id):
    if current_user.is_teacher:
        return redirect(url_for('teacher.dashboard'))
    
    exam = Exam.query.get_or_404(exam_id)
    total_score = 0
    max_score_per_question = 100 / len(exam.questions)
    
    for question in exam.questions:
        answer_text = request.form.get(f'answer_{question.id}')
        is_correct = False
        
        if question.question_type.value == 'multiple_choice':
            is_correct = answer_text == question.correct_answer
            if is_correct:
                total_score += max_score_per_question
        else:
            answer_similarity = similar(answer_text.lower(), question.correct_answer.lower())
            score_for_question = max_score_per_question * answer_similarity
            total_score += score_for_question
            is_correct = answer_similarity > 0.8
            
        student_answer = StudentAnswer(
            student_id=current_user.id,
            question_id=question.id,
            answer_text=answer_text,
            is_correct=is_correct
        )
        db.session.add(student_answer)
    
    score = Score(
        user_id=current_user.id,
        exam_id=exam_id,
        score=round(total_score)
    )
    db.session.add(score)
    db.session.commit()
    
    flash(f'Sınav tamamlandı. Skorunuz: {round(total_score)}')
    return redirect(url_for('student.dashboard'))

def similar(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()