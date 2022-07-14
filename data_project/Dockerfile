FROM python:3.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
EXPOSE 8000

COPY . /app

RUN pip install --upgrade pip &&  \
    pip install pipenv &&  \
    pipenv install --system --deploy --ignore-pipfile

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

