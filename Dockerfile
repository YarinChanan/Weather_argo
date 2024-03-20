FROM python:slim as build

RUN pip install requests
RUN pip install gunicorn
RUN pip install flask

#Stage two - creating second image: deploy

#using base image from phase 1
FROM build

WORKDIR /Weather_app

#copy app from host
COPY ./Project /Weather_app

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app:app

