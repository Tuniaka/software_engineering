REVISION := $(shell git rev-parse --short HEAD)
DOCKER_IMAGE_NAME = cr.yandex/crprpurksmdr58vchrr/bezlepkin:$(REVISION)

build:
	docker build --platform linux/amd64 -t $(DOCKER_IMAGE_NAME) . --file .Dockerfile

push:
	docker push $(DOCKER_IMAGE_NAME)

run:
	docker run --rm -e PORT=8080 -p 8080:8080 $(DOCKER_IMAGE_NAME)
