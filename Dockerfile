#FROM python:latest
FROM python:3.12.2 as dev

WORKDIR /usr/src/app
COPY . .


RUN pip install beautifulsoup4
RUN pip install selenium
RUN pip install pandas
RUN pip install sqlalchemy psycopg2

ENV SELENIUM_ADDR='http://sel:4444/wd/hub'


CMD ["bash", "-c", "while true; do sleep 3600; done"]

FROM dev as test

RUN pip install pytest

CMD ["bash", "-c", "pytest -v"]

FROM test as test_debug

CMD ["bash", "-c", "while true; do sleep 3600; done"]