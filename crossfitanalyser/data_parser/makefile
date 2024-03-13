
run_selenium:
	docker pull selenium/standalone-firefox
	docker run -it --name selenium -p 4444:4444 -v /dev/shm:/dev/shm -d selenium/standalone-firefox

build_dev:
	docker build -t data-parser-dev --target dev .
build_test:
	docker build -t data-parser-test --target test .
build_test_debug:
	docker build -t data-parser-test-debug --target test_debug .