FROM python:latest

WORKDIR /usr/src/app
COPY . .

RUN pip install beautifulsoup4
RUN pip install Scrapy

CMD ["bash", "-c", "while true; do sleep 3600; done"]