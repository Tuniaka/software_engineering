# Makefile для сборки, отправки и запуска Docker-образа веб-приложения Streamlit с распознаванием речи

# Получаем короткий хэш последнего коммита для тега образа
REVISION := $(shell git rev-parse --short HEAD)

# Определяем имя Docker-образа с тегом, основанным на хэше коммита
DOCKER_IMAGE_NAME = cr.yandex/crprpurksmdr58vchrr/bezlepkin:$(REVISION)

# Цель для сборки Docker-образа
build:
	docker build --platform linux/amd64 -t $(DOCKER_IMAGE_NAME) . --file .Dockerfile

# Цель для отправки Docker-образа в репозиторий
push:
	docker push $(DOCKER_IMAGE_NAME)

# Цель для запуска Docker-контейнера с образом
run:
	docker run --rm -it --device /dev/snd:/dev/snd -p 8501:8501 $(DOCKER_IMAGE_NAME)