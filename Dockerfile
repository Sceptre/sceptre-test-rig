FROM python:3.6.8-alpine3.9
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./tests /project
WORKDIR /project
ENTRYPOINT ["pytest"]
