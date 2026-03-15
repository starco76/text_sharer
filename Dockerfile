# استفاده از تصویر رسمی Python
FROM python:3.11-slim

# تنظیم دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل requirements (در ادامه می‌سازیم)
COPY requirements.txt .

# نصب پکیج‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کل پروژه به کانتینر
COPY . .
# expose پورت پیش‌فرض FastAPI
EXPOSE 8000

# اجرای اپ با uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]