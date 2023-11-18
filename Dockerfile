#FROM python:latest
FROM python:latest

WORKDIR /usr/src/app
COPY . .


RUN pip install beautifulsoup4
RUN pip install Scrapy
RUN pip install requests-html
RUN pip install selenium

CMD ["bash", "-c", "while true; do sleep 3600; done"]