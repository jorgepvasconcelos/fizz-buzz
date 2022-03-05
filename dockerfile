FROM python:3.8-slim-buster
COPY ./requirements.txt /var/www/requirements.txt
WORKDIR /var/www
RUN pip install -r requirements.txt
COPY ./fizz_buzz /var/www
CMD [ "python", "app.py" ]