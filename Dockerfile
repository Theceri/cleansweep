FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD gunicorn -b 0.0.0.0:5000 -w 2 cleansweep.wsgiapp:wsgi
