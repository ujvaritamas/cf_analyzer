# cf_analyzer
cf_analyzer

**commands for local testing:**   
python3 -m venv virtualenv   
source ./virtualenv/bin/activate  (win: .\virtualenv\Scripts\activate.bat)   
virtualenv\Scripts\python -m pip install --upgrade pip  
python -m pip install beautifulsoup4  
deactivate  

first: run selenium: https://hub.docker.com/r/selenium/standalone-firefox   


docker pull selenium/standalone-firefox   
docker run -d -p 4444:4444  --name sel -v /dev/shm:/dev/shm selenium-standalone-firefox   

docker build -t cf_analyser .   

docker run -d --name test -v $(pwd)/proj:/myapp cf_analyser   

Containers shall be on the same network   
docker network create myNetwork   
docker network connect myNetwork test   
docker network connect myNetwork sel   


or just run  
docker compose up -d  

docker compose -f docker-compose-dev.yml up -d   

docker compose down   

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb   

docker exec -it < contid > /bin/bash   

#delete docker : docker image prune -a, docker image prune -a, docker system prune --volumes   


make -C proj/ run_pytest   


https://docs.sqlalchemy.org/en/20/orm/quickstart.html   

/opt/homebrew/bin/brew install helm   
/opt/homebrew/bin/brew list helm   
alias helm='/opt/homebrew/Cellar/helm/3.14.2/bin/helm'   