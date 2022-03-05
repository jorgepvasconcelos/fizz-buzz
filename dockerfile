FROM python:3.8-slim-buster
COPY ./requirements.txt /aplicativo/requirements.txt
WORKDIR /aplicativo
RUN pip install -r requirements.txt
COPY ./fizz_buzz /aplicativo
CMD [ "python", "app.py" ]