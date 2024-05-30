"""
@brief Dockerfile для создания Docker-образа веб-приложения Streamlit с распознаванием речи.

@file Dockerfile
@author Rayzedan, sard-nas, Tuniaka
@date May 2024

Этот Dockerfile описывает сборку Docker-образа для веб-приложения Streamlit, которое использует SpeechRecognition для распознавания речи.
"""

# Используем образ Python версии 3.10 в качестве базового
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Обновляем пакеты и устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    curl \
    portaudio19-dev

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt requirements.txt

# Устанавливаем зависимости из requirements.txt
RUN pip3 install -r requirements.txt

# Копируем весь код приложения в рабочую директорию
COPY .. .

# Открываем порт 8501 для доступа к веб-приложению
EXPOSE 8501

# Определяем healthcheck для проверки работоспособности приложения
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Определяем команду для запуска веб-приложения Streamlit
ENTRYPOINT ["streamlit", "run", "web.py", "--server.port=8501", "--server.address=0.0.0.0"]