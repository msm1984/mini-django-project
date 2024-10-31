FROM python:alpine


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000


CMD python manage.py makemigrations && \
    python manage.py migrate --noinput && \
    python manage.py shell -c "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')" && \
    python manage.py runserver 0.0.0.0:8000

