"""
@brief Запускает веб-сервер для распознавания речи.

@file main.py
@author Rayzedan, sard-nas, Tuniaka
@date May 2024

Этот код запускает веб-сервер, используя код из файла api.py.
"""

import uvicorn
import os
from api import app

if __name__ == "__main__":
    """
    @brief Запускает веб-сервер с использованием Uvicorn.
    
    Сервер будет запущен на хосте "0.0.0.0" и порту, указанном в переменной окружения PORT (по умолчанию 8080).
    """
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")), log_level="info")