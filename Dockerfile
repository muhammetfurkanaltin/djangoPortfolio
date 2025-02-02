FROM python:3.11-slim

# PostgreSQL bağımlılıkları
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install watchdog Pillow  # Add this line to install watchdog and Pillow

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "py manage.py makemigrations && py manage.py migrate && watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- python manage.py runserver 0.0.0.0:8000"]