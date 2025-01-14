# Sınav Sistemi 🎓

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-brightgreen.svg)](https://flask.palletsprojects.com/en/3.0.x/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)

Öğretmenlerin sınav oluşturabileceği ve öğrencilerin ilgi alanlarına göre sınavlara katılabileceği bir Flask web uygulaması.

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
git clone https://github.com/username/exam-system.git
cd exam-system
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
| 👨‍🏫 Öğretmen | teacher1 | 123456 |
| 👨‍🎓 Öğrenci | student1 | 123456 |

## 📁 Proje Yapısı

```
exam-system/
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── __init__.py
├── migrations/
├── venv/
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── seed.py
```

## 🔧 Geliştirme

```bash
# Yeni branch oluştur
git checkout -b feature/yeni-ozellik

# Değişiklikleri commit et
git add .
git commit -m "Yeni özellik: açıklama"

# Branch'i push et
git push origin feature/yeni-ozellik
```

## ❗ Hata Durumunda

Olası hata çözümleri:

1. **Virtual environment aktif mi?**
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

2. **Paketler güncel mi?**
```bash
pip install -r requirements.txt
```

3. **Migration'lar güncel mi?**
```bash
flask db upgrade
```

4. **Veritabanını sıfırlama:**
```bash
# Windows
del instance/exam_system.db
# Linux/macOS
rm instance/exam_system.db

# Yeniden oluştur
flask db upgrade
python seed.py
```

## 🤝 Katkıda Bulunma

1. Fork'layın
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Commit'leyin (`git commit -m 'Yeni özellik eklendi'`)
4. Push'layın (`git push origin feature/YeniOzellik`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

## 📧 İletişim

Reşit - [@github](https://github.com/username)

Proje Linki: [https://github.com/username/exam-system](https://github.com/username/exam-system)

---
⭐️ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
