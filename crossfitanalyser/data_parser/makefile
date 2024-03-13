
#https://github.com/SeleniumHQ/docker-selenium
run_selenium:
#	docker pull selenium/standalone-firefox
#	docker run -it --name selenium -p 4444:4444 -v /dev/shm:/dev/shm -d selenium/standalone-firefox
#	docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" --name selenium selenium/standalone-firefox:4.3.0-20220726
# 	docker run -p 4444:4444 --name selenium --network parser_network selenium/standalone-firefox:4.3.0-20220726
	docker network create parser_network
	docker run -d --name selenium --network parser_network selenium/standalone-firefox:4.3.0-20220726
	


build_dev:
	docker build -t data-parser-dev --target dev .
build_test:
	docker build -t data-parser-test --target test .
build_test_debug:
	docker build -t data-parser-test-debug --target test_debug .

run_dev:
#	if network not created the parser need to be run on the host network to reach the selenium port
	docker network create selenium-net --driver bridge
	docker run -d --name parser-dev --network host data-parser-dev