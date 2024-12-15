FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.prod.txt /app/requirements.prod.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.prod.txt

COPY . .
ENV DJANGO_SETTINGS_MODULE=settings.production
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]