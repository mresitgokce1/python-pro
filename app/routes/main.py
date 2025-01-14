from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.is_teacher:
            return redirect(url_for('teacher.dashboard'))
        return redirect(url_for('student.dashboard'))
    return render_template('index.html')