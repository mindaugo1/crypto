# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /app
COPY ./requirements.txt .
COPY ./cur_project/ ./cur_project/
RUN pip install -r requirements.txt
WORKDIR /app/cur_project
# RUN python manage.py collectstatic --noinput
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "drf_api_project.wsgi"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
