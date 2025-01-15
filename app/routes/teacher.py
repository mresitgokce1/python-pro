from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Interest, Exam, Question, QuestionType
from app import db
import json

from app.models.options import QuestionOption
from app.models.score import Score
from app.models.student_answer import StudentAnswer
from app.models.user import User

bp = Blueprint('teacher', __name__, url_prefix='/teacher')

@bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_teacher:
        flash('Bu sayfaya erişim yetkiniz yok.')
        return redirect(url_for('main.index'))
        
    exams = Exam.query.filter_by(created_by=current_user.id).all()
    return render_template('teacher/dashboard.html', exams=exams)

@bp.route('/interests', methods=['GET'])
@login_required
def list_interests():
    if not current_user.is_teacher:
        flash('Bu sayfaya erişim yetkiniz yok.')
        return redirect(url_for('main.index'))
    
    interests = Interest.query.all()
    return render_template('teacher/interests.html', interests=interests)

@bp.route('/interests/add', methods=['GET', 'POST'])
@login_required
def add_interest():
    if not current_user.is_teacher:
        return redirect(url_for('main.index'))
        
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            interest = Interest(name=name, created_by=current_user.id)
            db.session.add(interest)
            db.session.commit()
            flash('İlgi alanı başarıyla eklendi.')
            return redirect(url_for('teacher.list_interests'))
            
    return render_template('teacher/add_interest.html')

@bp.route('/exam/create', methods=['GET', 'POST'])
@login_required
def create_exam():
    if not current_user.is_teacher:
        return redirect(url_for('main.index'))
    
    interests = Interest.query.all()
    
    if request.method == 'POST':
        title = request.form.get('title')
        interest_id = request.form.get('interest_id')
        
        exam = Exam(
            title=title,
            interest_id=interest_id,
            created_by=current_user.id
        )
        db.session.add(exam)
        db.session.flush()  # ID'yi almak için flush

        question_data = []
        i = 0
        while f'questions[{i}][text]' in request.form:
            question = {
                'text': request.form.get(f'questions[{i}][text]'),
                'type': request.form.get(f'questions[{i}][type]'),
                'correct_answer': request.form.get(f'questions[{i}][correct_answer]'),
                'options': {
                    label: request.form.get(f'questions[{i}][options][{label}]')
                    for label in ['A', 'B', 'C', 'D']
                    if request.form.get(f'questions[{i}][options][{label}]')
                } if request.form.get(f'questions[{i}][type]') == 'multiple_choice' else None
            }
            question_data.append(question)
            i += 1
        
        for data in question_data:
            question = Question(
                exam_id=exam.id,
                question_text=data['text'],
                question_type=QuestionType(data['type']),
                correct_answer=data['correct_answer']
            )
            db.session.add(question)
            db.session.flush()  # Question ID'yi almak için

            if data['type'] == 'multiple_choice' and data['options']:
                for label, text in data['options'].items():
                    option = QuestionOption(
                        question_id=question.id,
                        option_label=label,
                        option_text=text
                    )
                    db.session.add(option)
        
        db.session.commit()
        flash('Sınav başarıyla oluşturuldu!')
        return redirect(url_for('teacher.dashboard'))
        
    return render_template('teacher/create_exam.html', interests=interests)

@bp.route('/exam/delete/<int:exam_id>', methods=['POST'])
@login_required
def delete_exam(exam_id):
    if not current_user.is_teacher:
        flash('Bu işlem için yetkiniz yok.', 'danger')
        return redirect(url_for('main.index'))
    
    exam = Exam.query.get_or_404(exam_id)
    
    if exam.created_by != current_user.id:
        flash('Bu sınavı silme yetkiniz yok.', 'danger')
        return redirect(url_for('teacher.dashboard'))
    
    try:
        questions = Question.query.filter_by(exam_id=exam.id).all()
        for question in questions:
            StudentAnswer.query.filter_by(question_id=question.id).delete()
        
        Score.query.filter_by(exam_id=exam.id).delete()
        
        Question.query.filter_by(exam_id=exam.id).delete()
        
        db.session.delete(exam)
        db.session.commit()
        
        flash('Sınav başarıyla silindi.', 'success')
    except Exception as e:
        print(str(e))
        db.session.rollback()
        flash('Sınav silinirken bir hata oluştu.', 'danger')
        
    return redirect(url_for('teacher.dashboard'))


@bp.route('/exam/detail/<int:exam_id>')
@login_required
def exam_detail(exam_id):
    if not current_user.is_teacher:
        flash('Bu işlem için yetkiniz yok.', 'danger')
        return redirect(url_for('main.index'))
    
    exam = Exam.query.options(
        db.joinedload(Exam.questions).joinedload(Question.options)
    ).get_or_404(exam_id)
    
    if exam.created_by != current_user.id:
        flash('Bu sınava erişim yetkiniz yok.', 'danger')
        return redirect(url_for('teacher.dashboard'))
    
    student_scores = {}
    for score in exam.scores:
        student = User.query.get(score.user_id)
        if student.id not in student_scores:
            student_scores[student.id] = {
                'username': student.username,
                'scores': []
            }
        student_scores[student.id]['scores'].append(score.score)

    return render_template('teacher/exam_detail.html', 
                         exam=exam, 
                         student_scores=student_scores)

@bp.route('/interest/delete/<int:interest_id>', methods=['POST'])
@login_required
def delete_interest(interest_id):
    interest = Interest.query.get_or_404(interest_id)
    
    try:
        db.session.delete(interest)
        db.session.commit()
        flash('İlgi alanı başarıyla silindi.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('İlgi alanı silinirken bir hata oluştu.', 'danger')
        
    return redirect(url_for('teacher.list_interests'))