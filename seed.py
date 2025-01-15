from app import create_app, db
from app.models import User, Interest, Exam, Question, QuestionType, QuestionOption
from datetime import datetime

def seed_database():
   app = create_app()
   with app.app_context():
       try:
           db.drop_all()
           db.create_all()

           # Kullanıcılar
           teacher = User(
               username='teacher',
               email='teacher@example.com',
               is_teacher=True
           )
           teacher.set_password('123123123')
           db.session.add(teacher)
           db.session.flush()

           student = User(
               username='student',
               email='student@example.com',
               is_teacher=False
           )
           student.set_password('123123123')
           db.session.add(student)
           db.session.flush()

           # İlgi alanları ve sınavlar
           interests_and_exams = [
               {
                   'name': "Python'da AI geliştirme",
                   'exam': {
                       'title': "Python'da AI Temel Kavramlar Sınavı",
                       'questions': [
                           {
                               'text': 'Yapay zekada supervised ve unsupervised learning arasındaki temel fark nedir?',
                               'type': QuestionType.TEXT,
                               'answer': 'Supervised learning etiketli veri kullanırken, unsupervised learning etiketsiz veri kullanır.',
                               'options': []
                           },
                           {
                               'text': 'Hangisi Python\'da yapay zeka için kullanılan bir kütüphane değildir?',
                               'type': QuestionType.MULTIPLE_CHOICE,
                               'answer': 'C',
                               'options': [
                                   {'label': 'A', 'text': 'TensorFlow'},
                                   {'label': 'B', 'text': 'PyTorch'},
                                   {'label': 'C', 'text': 'BeautifulSoup'},
                                   {'label': 'D', 'text': 'Scikit-learn'}
                               ]
                           }
                       ]
                   }
               },
               {
                   'name': 'Bilgisayar Görüşü',
                   'exam': {
                       'title': 'Bilgisayar Görüşü Değerlendirme',
                       'questions': [
                           {
                               'text': 'OpenCV kullanarak görüntü işlemede kenar tespitinin önemini ve kullanım alanlarını açıklayınız.',
                               'type': QuestionType.TEXT,
                               'answer': 'Kenar tespiti, görüntülerdeki nesnelerin sınırlarını belirlemede ve nesne tanıma sistemlerinde önemli bir adımdır. Güvenlik sistemleri, medikal görüntüleme ve robotik gibi alanlarda kullanılır.',
                               'options': []
                           },
                           {
                               'text': 'Aşağıdakilerden hangisi görüntü gürültüsünü azaltmak için kullanılan bir filtredir?',
                               'type': QuestionType.MULTIPLE_CHOICE,
                               'answer': 'A',
                               'options': [
                                   {'label': 'A', 'text': 'Gaussian Blur'},
                                   {'label': 'B', 'text': 'Sobel Operatörü'},
                                   {'label': 'C', 'text': 'Canny Dedektörü'},
                                   {'label': 'D', 'text': 'Threshold'}
                               ]
                           }
                       ]
                   }
               },
               {
                   'name': 'NLP (Nöro-dilbilim)',
                   'exam': {
                       'title': 'NLP Temel Kavramlar Sınavı',
                       'questions': [
                           {
                               'text': 'NLP\'de tokenization işleminin önemini ve kullanım alanlarını detaylı açıklayınız.',
                               'type': QuestionType.TEXT,
                               'answer': 'Tokenization, metni anlamlı parçalara (token) ayırma işlemidir. Cümle analizi, duygu analizi ve makine çevirisi gibi NLP uygulamalarında temel bir ön işleme adımıdır.',
                               'options': []
                           },
                           {
                               'text': 'Aşağıdakilerden hangisi duygu analizi (sentiment analysis) için kullanılan bir yaklaşım değildir?',
                               'type': QuestionType.MULTIPLE_CHOICE,
                               'answer': 'D',
                               'options': [
                                   {'label': 'A', 'text': 'Lexicon-based approach'},
                                   {'label': 'B', 'text': 'Machine Learning approach'},
                                   {'label': 'C', 'text': 'Deep Learning approach'},
                                   {'label': 'D', 'text': 'Fourier Transform'}
                               ]
                           }
                       ]
                   }
               },
               {
                   'name': 'Python uygulamalarında AI modelleri uygulama',
                   'exam': {
                       'title': 'AI Model Deployment Sınavı',
                       'questions': [
                           {
                               'text': 'Bir yapay zeka modelini production ortamına deploy ederken dikkat edilmesi gereken faktörleri detaylı açıklayınız.',
                               'type': QuestionType.TEXT,
                               'answer': 'Model performansı, ölçeklenebilirlik, kaynak yönetimi, güvenlik ve monitoring en önemli faktörlerdir. Ayrıca model versiyonlama ve A/B testing stratejileri de göz önünde bulundurulmalıdır.',
                               'options': []
                           },
                           {
                               'text': 'Aşağıdakilerden hangisi model optimizasyonu için kullanılan bir teknik değildir?',
                               'type': QuestionType.MULTIPLE_CHOICE,
                               'answer': 'C',
                               'options': [
                                   {'label': 'A', 'text': 'Hyperparameter tuning'},
                                   {'label': 'B', 'text': 'Model pruning'},
                                   {'label': 'C', 'text': 'Database indexing'},
                                   {'label': 'D', 'text': 'Feature selection'}
                               ]
                           }
                       ]
                   }
               }
           ]

           # İlgi alanları, sınavlar ve soruları ekle
           interests = []
           for item in interests_and_exams:
               # İlgi alanı oluştur
               interest = Interest(name=item['name'], created_by=teacher.id)
               db.session.add(interest)
               db.session.flush()
               interests.append(interest)

               # Sınav oluştur
               exam = Exam(
                   title=item['exam']['title'],
                   interest_id=interest.id,
                   created_by=teacher.id
               )
               db.session.add(exam)
               db.session.flush()

               # Soruları ekle
               for q in item['exam']['questions']:
                   question = Question(
                       exam_id=exam.id,
                       question_text=q['text'],
                       question_type=q['type'],
                       correct_answer=q['answer']
                   )
                   db.session.add(question)
                   db.session.flush()

                   # Çoktan seçmeli soru şıklarını ekle
                   if q['type'] == QuestionType.MULTIPLE_CHOICE:
                       for opt in q['options']:
                           option = QuestionOption(
                               question_id=question.id,
                               option_label=opt['label'],
                               option_text=opt['text']
                           )
                           db.session.add(option)

           # Öğrenciye ilk 2 ilgi alanını ata
           student.interests = interests[:2]

           db.session.commit()

       except Exception as e:
           print(f"Hata: {str(e)}")
           db.session.rollback()
           raise

if __name__ == '__main__':
   seed_database()