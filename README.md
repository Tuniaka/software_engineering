## Участники команды
- Безлепкин Даниил
- Войнов Артём
- Хусаинова Александра

Библиотека: https://pypi.org/project/SpeechRecognition/

### Описание
SpeechRecognition - это библиотека для распознавания речи с поддержкой нескольких движков и API, онлайн и оффлайн.
В нашем решеннии используется Google Speech API.

### Пример использования

```python
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
	audio = recognizer.listen(source)
text = recognizer.recognize_google(audio, language="ru-RU")
print(text)
```

### Документация
Код в проекте прокомментирован в стиле DOXYGEN, что обеспечивает ясность и понимание функциональности каждого метода и класса. 
DOXYGEN - это инструмент для генерации документации на основе комментариев в коде.

### Архитектура проекта
#### WEB
Для реализации используется библиотека streamlit версии 1.29.0

#### API
Для реализации используется библиотека FastAPI версии 0.87.0

#### CI/CD
CI/CD реализован на базе `GitHub Actions`, запуск происходит при каждом `push` в репозиторий

#### Dependencies
Зависимости для модуля `API` описаны в файле `requirements.txt`, при запуске `Dockerfile` он парсится и подгружаются пакеты нужной версии

### Запуск Docker
```bash
cd api/ && make build && make run
```
Сервер будет запущен по адресу ```http://0.0.0.0:8080```
