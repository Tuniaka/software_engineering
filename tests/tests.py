"""
@brief Тестирование веб-приложения Streamlit с распознаванием речи.

@file test_api.py
@author Rayzedan, sard-nas, Tuniaka
@date May 2024

Этот код содержит тесты для веб-приложения Streamlit с распознаванием речи.
"""

import unittest
from unittest.mock import patch
import speech_recognition as sr
from fastapi.testclient import TestClient
from api.api import app

class TestSpeechRecognition(unittest.TestCase):

    def setUp(self):
        """
        @brief Инициализация клиента для тестирования.
        
        Создает клиент для тестирования веб-приложения.
        """
        self.client = TestClient(app)

    @patch('api.api.sr.Microphone')
    @patch('api.api.sr.Recognizer.listen')
    @patch('api.api.sr.Recognizer.recognize_google')
    def test_record_voice_success(self, mock_recognize_google, mock_listen, mock_microphone):
        """
        @brief Тестирование успешного распознавания речи.
        
        Проверяет, что при успешном распознавании речи возвращается текст и статус 200.
        """
        mock_listen.return_value = 'audio_data'
        mock_recognize_google.return_value = 'Hello, world'

        response = self.client.get('/record')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'text': 'Hello, world'})

    @patch('api.api.sr.Microphone')
    @patch('api.api.sr.Recognizer.listen')
    @patch('api.api.sr.Recognizer.recognize_google')
    def test_record_voice_unrecognized(self, mock_listen, mock_recognize_google, mock_microphone):
        """
        @brief Тестирование неуспешного распознавания речи.
        
        Проверяет, что при неуспешном распознавании речи возвращается ошибка и статус 200.
        """
        mock_listen.return_value = 'audio_data'
        mock_recognize_google.side_effect = sr.UnknownValueError('Speech not recognized')

        response = self.client.get('/record')
        self.assertRaises(sr.UnknownValueError)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'error': 'Речь не распознана'})

    @patch('api.api.sr.Microphone')
    @patch('api.api.sr.Recognizer.listen')
    @patch('api.api.sr.Recognizer.recognize_google')
    def test_record_voice_error(self, mock_recognize_google, mock_listen, mock_microphone):
        """
        @brief Тестирование ошибки распознавания речи.
        
        Проверяет, что при ошибке распознавания речи возвращается ошибка и статус 200.
        """
        mock_listen.return_value = 'audio_data'
        mock_recognize_google.side_effect = Exception('Unknown error')

        response = self.client.get('/record')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'error': 'Неизвестная ошибка: error'})


if __name__ == '__main__':
    unittest.main()