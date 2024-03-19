FROM python:slim as build

COPY ./Project/requirements.txt .

RUN pip install -r requirements.txt

#Stage two - creating second image: deploy

#using base image from phase 1
FROM build

WORKDIR /Weather_app

#copy app from host
COPY ./Project /Weather_app

EXPOSE 5000

CMD python app.py
