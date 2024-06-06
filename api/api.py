"""
@brief Простой веб-сервер для распознавания речи с использованием FastAPI и SpeechRecognition.

@file api.py
@author Rayzedan, sard-nas, Tuniaka
@date May 2024

Этот код представляет собой простой веб-сервер с использованием FastAPI для распознавания речи через микрофон
с помощью библиотеки SpeechRecognition.
"""

import speech_recognition as sr
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """
    @brief Возвращает сообщение "Распознавание речи".

    @return Словарь с сообщением.
    """
    return {"message": "Распознавание речи"}


@app.get("/record")
async def record_voice():
    """
    @brief Записывает речь с микрофона, пытается распознать ее с помощью Google Speech Recognition API на русском языке
    и возвращает распознанный текст или сообщение об ошибке.

    @return Словарь с распознанным текстом или сообщением об ошибке.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source, timeout=5.0)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        return {"text": text}
    except sr.UnknownValueError:
        return {"error": "Речь не распознана"}
    except BaseException:
        return {"error": "Неизвестная ошибка: error"}
