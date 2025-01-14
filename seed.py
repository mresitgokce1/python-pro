from app import create_app, db
from app.models import User, Interest


def seed_database():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        teacher = User(
            username='teacher',
            email='teacher@example.com',
            is_teacher=True
        )
        teacher.set_password('123456')
        db.session.add(teacher)

        interests = [
            Interest(name="Python'da AI geliştirme", created_by=1),
            Interest(name='Bilgisayar Görüşü', created_by=1),
            Interest(name='NLP (Nöro-dilbilim)', created_by=1),
            Interest(name='Python uygulamalarında AI modelleri uygulama', created_by=1),
        ]

        for interest in interests:
            db.session.add(interest)

        db.session.commit()

if __name__ == '__main__':
    seed_database()
    