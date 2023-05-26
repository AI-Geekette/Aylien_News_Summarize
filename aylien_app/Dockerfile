# Dockerfile

# pull the official docker image
#FROM python:3.9.4-slim
FROM python:3.8-slim

# set work directory
WORKDIR /aylien_app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY aylien_requirements.txt .
RUN pip install -r aylien_requirements.txt
RUN pip install --upgrade urllib3


# copy project
COPY . .

CMD [ "uvicorn", "main:app", "--reload"]
