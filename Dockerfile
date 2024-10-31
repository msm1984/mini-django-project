FROM python:3.10-alpine as builder


RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev


WORKDIR /app


COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt


FROM python:3.10-alpine


RUN apk update && \
    apk add --no-cache libpq


WORKDIR /app


COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*


COPY . .


EXPOSE 8000


CMD python manage.py makemigrations && \
    python manage.py migrate --noinput && \
    python manage.py shell -c "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')" && \
    python manage.py runserver 0.0.0.0:8000

