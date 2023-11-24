help:
	echo "build, up, run, debug, down, clean"
build:
	docker compose -f docker-compose-dev.yaml build
rebuild_up: down test_down clean build up
up:
	docker compose -f docker-compose-dev.yaml up -d
run:
	docker compose -f docker-compose-dev.yaml run --rm sel
debug:
	docker compose -f docker-compose-dev.yaml exec cf_analyser_dev /bin/bash
down:
	docker compose -f docker-compose-dev.yaml down
clean:
	docker image prune -a; docker system prune -a --volumes;
test_log:
	docker logs cf_analyser_test

test_down_clean: down clean
test_up_unittest:
	docker compose -f docker-compose-test.yaml up -d
test_run: test_down_clean test_up_unittest
test_down:
	docker compose -f docker-compose-test.yaml down

test_debug_up:
	docker compose -f docker-compose-test_debug.yaml up -d
test_debug_debug:
	docker compose -f docker-compose-test_debug.yaml exec cf_analyser_test_debug /bin/bash
test_debug_down:
	docker compose -f docker-compose-test_debug.yaml down
test_debug_clean: test_debug_down clean

