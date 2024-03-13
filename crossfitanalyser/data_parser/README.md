# Steps
(TODO)
1. `docker network create parser_network --driver bridge`   create network

2. `docker run -d --name selenium -p 4444:4444 --network parser_network selenium/standalone-firefox:4.3.0-20220726` run selenium

3. `docker build -t data-parser-dev --target dev .` run the service

4. 3. `docker run -d --name data-parser --network parser_network data-parser-dev` run the service