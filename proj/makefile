run_pytest:
	PYTHONPATH=./src pytest
	echo ${PYTHONPATH}
	pytest -v

run_test:
	pytest -v
run_test_with_path:
	pytest --basetemp=tests/temp
	echo "Remove base temp dir"
	rm -rf tests/temp