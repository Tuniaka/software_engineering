## Участники команды
- Безлепкин Даниил
- Войнов Артём
- Хусаинова Александра 

Библиотека: https://pypi.org/project/SpeechRecognition/

### Описание
SpeechRecognition - это библиотека для распознавания речи с поддержкой нескольких движков и API, онлайн и оффлайн.
В нашем решеннии используется Google Speech API.

### Пример использования

import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
	audio = recognizer.listen(source)
text = recognizer.recognize_google(audio, language="ru-RU")
print(text)