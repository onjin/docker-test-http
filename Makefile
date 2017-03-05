.PHONY: test-app run
DEFAULT: test-app

test-app:
	docker build -t test-app .

run: test-app
	docker run -it --rm -p 8888:8888 -e TEST_APP=True test-app
