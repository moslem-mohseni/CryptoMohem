# CryptoMohem

**یک وبسایت خبری هوشمند با اتوماسیون کامل در حوزه رمزارزها**

CryptoMohem یک پلتفرم خبری است که به صورت کاملا خودکار اخبار را از منابع معتبر جمع‌آوری، ترجمه، تصویرسازی و منتشر می‌کند.

## ویژگی‌های کلیدی

- 🤖 **اتوماسیون کامل**: بدون نیاز به ادمین برای تولید محتوا
- 🌐 **چندمنبعی**: کرال از وبسایت‌ها و کانال‌های تلگرام
- 🧠 **هوش مصنوعی**: ترجمه، خلاصه‌سازی، تحلیل احساسات، امتیازدهی
- 🎨 **تولید تصویر**: ساخت خودکار تصویر با AI
- 📱 **PWA**: قابل نصب بر روی موبایل
- ⚙️ **قابل تنظیم**: تغییر منابع، حوزه فعالیت و تنظیمات از پنل ادمین

## تکنولوژی‌ها

- **Backend**: Django 5.0+, PostgreSQL, Redis, Celery
- **AI**: Google Gemini API, Stable Diffusion
- **Frontend**: Django Templates, Tailwind CSS, Alpine.js
- **DevOps**: Docker, Docker Compose, Nginx, Gunicorn

## نصب و راه‌اندازی

### پیش‌نیازها

- Docker و Docker Compose
- Git

### راه‌اندازی با Docker (توصیه می‌شود)

1. کلون کردن پروژه:
```bash
git clone https://github.com/yourusername/CryptoMohem.git
cd CryptoMohem
```

2. کپی کردن فایل محیطی:
```bash
cp .env.example .env
```

3. ویرایش `.env` و تنظیم متغیرهای محیطی (اختیاری برای شروع)

4. بیلد و اجرای کانتینرها:
```bash
docker-compose up --build
```

5. در یک ترمینال دیگر، ایجاد superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

6. دسترسی به برنامه:
- وبسایت: http://localhost:8000
- پنل ادمین: http://localhost:8000/admin

### راه‌اندازی بدون Docker (Development)

1. ایجاد محیط مجازی:
```bash
python3 -m venv venv
source venv/bin/activate  # در Windows: venv\Scripts\activate
```

2. نصب dependencies:
```bash
pip install -r requirements.txt
```

3. نصب PostgreSQL و Redis:
```bash
# Ubuntu/Debian
sudo apt-get install postgresql redis-server

# macOS
brew install postgresql redis
```

4. ایجاد دیتابیس:
```bash
sudo -u postgres createdb cryptomohem
```

5. تنظیم `.env` با مقادیر مناسب (DB_HOST=localhost)

6. اجرای migrations:
```bash
python manage.py migrate
```

7. ایجاد superuser:
```bash
python manage.py createsuperuser
```

8. اجرای سرور:
```bash
python manage.py runserver
```

9. در ترمینال‌های جداگانه، اجرای Celery:
```bash
# Worker
celery -A config worker -l info

# Beat
celery -A config beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## ساختار پروژه

```
CryptoMohem/
├── config/              # تنظیمات اصلی Django
│   ├── settings/        # تنظیمات محیط‌های مختلف
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── celery.py
├── apps/                # اپلیکیشن‌های Django (در فازهای بعدی)
├── static/              # فایل‌های استاتیک
├── media/               # فایل‌های آپلود شده
├── templates/           # قالب‌های HTML
├── requirements.txt     # وابستگی‌های Python
├── Dockerfile
├── docker-compose.yml
└── manage.py

```

## دستورات مهم

```bash
# مشاهده logs
docker-compose logs -f

# ری‌استارت سرویس‌ها
docker-compose restart

# متوقف کردن
docker-compose down

# پاک کردن volumes
docker-compose down -v

# اجرای migrations
docker-compose exec web python manage.py migrate

# جمع‌آوری static files
docker-compose exec web python manage.py collectstatic --noinput
```

## وضعیت پروژه

✅ **فاز 1 (کامل شد)**: راه‌اندازی اولیه Django + Docker + PostgreSQL + Redis

🔄 **در حال توسعه**: فازهای 2 تا 15 (مطابق `todo.me`)

## مستندات

برای اطلاعات بیشتر، فایل `todo.me` را مطالعه کنید که شامل:
- معماری کامل سیستم
- مدل‌های دیتابیس
- فازبندی پروژه (15 فاز)
- امکانات نهایی

## مجوز

This project is licensed under the MIT License.

## نکته مهم

این پروژه به گونه‌ای طراحی شده که می‌تواند برای **هر حوزه خبری دیگری** نیز استفاده شود. کدنویسی Generic و قابل استفاده مجدد است.
