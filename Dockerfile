FROM python:3.9.0

WORKDIR /home/

RUN echo "test21.08.06.22-2"

RUN git clone https://github.com/Minjaehyun/pinterest.git

WORKDIR /home/pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pinterest.settings.deploy && python manage.py collectstatic --noinput --settings=pinterest.settings.deploy && gunicorn pinterest.wsgi --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy --bind 0.0.0.0:8000"]