# cf_analyzer
cf_analyzer

commands:
python3 -m venv virtualenv
source ./virtualenv/bin/activate  (win: .\virtualenv\Scripts\activate.bat)
virtualenv\Scripts\python -m pip install --upgrade pip
python -m pip install beautifulsoup4
deactivate


docker build -t cf_analyser .

docker run -d --name test -v $(pwd)/proj:/myapp cf_analyser

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

docker exec -it < contid > /bin/bash

#delete docker : docker image prune -a, docker image prune -a, docker system prune --volumes