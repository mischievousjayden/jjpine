
build:
	sudo docker build -f ops/docker/dockerfile --build-arg COMMIT=master -t jjpine:local ops/docker

test:
	pytest test
