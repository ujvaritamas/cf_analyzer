#FROM python:latest
FROM python:latest as dev

WORKDIR /usr/src/app
COPY . .


#RUN pip install beautifulsoup4
#RUN pip install selenium
#RUN pip install pandas
#RUN pip install sqlalchemy psycopg2

#RUN pip install -r requirements.txt --no-cache-dir



CMD ["bash", "-c", "while true; do sleep 3600; done"]

FROM dev as test

RUN pip install pytest

CMD ["bash", "-c", "pytest -v"]

FROM test as test_debug

CMD ["bash", "-c", "while true; do sleep 3600; done"]