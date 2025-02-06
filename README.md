# Sınav Sistemi 🎓

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-brightgreen.svg)](https://flask.palletsprojects.com/en/3.0.x/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)

Öğretmenlerin sınav oluşturabileceği ve öğrencilerin ilgi alanlarına göre sınavlara katılabileceği bir Flask web uygulaması.

## Canlı Linki
- https://mrgokce.pythonanywhere.com/

## 🚀 Özellikler

- ✅ Öğretmen ve öğrenci girişi
- 📚 İlgi alanlarına göre sınav kategorileri
- 📝 Çoktan seçmeli ve yazılı soru tipleri
- 📊 Öğrenci skorlarının takibi
- 📈 Sınav sonuçlarının detaylı analizi

## 🛠️ Kurulum

### Gereksinimler

- Python 3.9 veya üzeri
- pip (Python paket yöneticisi)

### Adım Adım Kurulum

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/mresitgokce1/python-pro.git
cd python-pro
```

2. **Virtual environment oluşturun:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. **Gereksinimleri yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Veritabanını oluşturun:**
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

5. **Örnek verileri yükleyin:**
```bash
python seed.py
```

6. **Uygulamayı başlatın:**
```bash
python run.py
```

Uygulama [http://localhost:5000](http://localhost:5000) adresinde çalışacaktır.

## 👥 Test Hesapları

| Rol | Kullanıcı Adı | Şifre |
|-----|---------------|-------|
| 👨‍🏫 Öğretmen | teacher | 123123123 |
| 👨‍🎓 Öğrenci | student | 123123123 |

## 📁 Proje Yapısı

```
exam-system/
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   └── __init__.py
├── migrations/
├── venv/
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── seed.py
```
