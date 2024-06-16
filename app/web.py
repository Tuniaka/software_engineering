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
import base64
import time


class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = False

    def recognize(self, source):
        """
        @brief Запускает распознавание речи через микрофон.

        @param source: Микрофон для записи.
        @return Распознанный текст или сообщение об ошибке.
        """
        self.recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = self.recognizer.listen(source, timeout=5.0)
        try:
            text = self.recognizer.recognize_google(audio, language="ru-RU")
            return text
        except sr.UnknownValueError:
            return "Речь не распознана"
        except BaseException as error:
            print('Неизвестная ошибка: {}'.format(error))
            return "Ошибка: неизвестная ошибка"


class VoiceRecognitionApp:
    def __init__(self):
        self.speech_recognition = SpeechRecognition()

    def on_copy_click(self, text):
        """
        @brief Копирует текст в буфер обмена и выводит уведомление.

        @param text: Текст для копирования.
        """
        pyperclip.copy(text)
        st.toast(f"Скопировано в буфер обмена: {text}", icon='✅')

    def on_save_click(self, text):
        """
        @brief Копирует текст в файл и предоставляет ссылку для скачивания файла.

        @param text: Текст для копирования.
        """
        b64 = base64.b64encode(text.encode()).decode()
        filename = "recognized_text"
        timestr = time.strftime("%Y%m%d-%H%M%S")
        new_filename = "{}_{}_.txt".format(filename, timestr)
        st.markdown("#### Загрузка файла ###")
        href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Ссылка для скачивания</a>'
        st.markdown(href, unsafe_allow_html=True)

    def command(self):
        """
        @brief Запускает распознавание речи через микрофон.

        @return Распознанный текст или сообщение об ошибке.
        """
        with sr.Microphone() as source:
            st.write("Слушаю голос...")
            text = self.speech_recognition.recognize(source)
        return text

    def create_web(self):
        """
        @brief Создает веб-интерфейс для записи и распознавания речи.
        """
        st.title("Распознавание речи")
        st.write("Нажмите кнопку, чтобы записать голос")

        if st.button("Записать голос"):
            text = self.command()
            if text:
                st.write("Текст:", text)
                right, left = st.columns([1, 6])
                with right:
                    st.button("📋", on_click=self.on_copy_click, args=(text,))
                with left:
                    st.button("📥", on_click=self.on_save_click, args=(text,))


if __name__ == '__main__':
    app = VoiceRecognitionApp()
    app.create_web()
