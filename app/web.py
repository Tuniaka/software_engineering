"""
@brief Простое веб-приложение для распознавания речи с использованием SpeechRecognition и Streamlit.

@file voice_recognition_app.py
@author Rayzedan, sard-nas, Tuniaka
@date May 2024

Этот код представляет собой веб-приложение для распознавания речи через микрофон
с использованием библиотек SpeechRecognition и Streamlit.
"""

import speech_recognition as sr
import streamlit as st
import pyperclip


def on_copy_click(text):
    """
    @brief Копирует текст в буфер обмена и выводит уведомление.

    @param text: Текст для копирования.
    """
    pyperclip.copy(text)
    st.toast(f"Скопировано в буфер обмена: {text}", icon='✅')


def command():
    """
    @brief Запускает распознавание речи через микрофон.

    @return Распознанный текст или сообщение об ошибке.
    """
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    with sr.Microphone() as source:
        st.write("Слушаю голос...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5.0)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        return text
    except sr.UnknownValueError:
        st.write("Речь не распознана")
    except BaseException as error:
        print('Неизвестная ошибка: {}'.format(error))


def create_web():
    """
    @brief Создает веб-интерфейс для записи и распознавания речи.
    """
    st.title("Распознавание речи")
    st.write("Нажмите кнопку, чтобы записать голос")

    if st.button("Записать голос"):
        text = command()
        if text:
            st.write("Текст:", text)
            st.button("📋", on_click=on_copy_click, args=(text,))
        else:
            st.write("Ошибка: речь не распознана")


if __name__ == '__main__':
    create_web()
