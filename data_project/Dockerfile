FROM python:3.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/ds_project

COPY ./Pipfile.lock /usr/src/ds_project
COPY ./Pipfile /usr/src/ds_project

RUN pip install pipenv && pipenv install

COPY . /usr/src/ds_project

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




