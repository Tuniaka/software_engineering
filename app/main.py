"""
@brief Запуск веб-приложения Streamlit.

@file app.py
@author Rayzedan, sard-nas, Tuniaka
@date May 2024

Этот код запускает веб-приложение Streamlit с указанными параметрами.
"""

from streamlit.web.cli import main
import sys

if __name__ == "__main__":
    """
    @brief Запускает веб-приложение Streamlit с определенными параметрами.

    Устанавливает аргументы командной строки для запуска Streamlit с указанным портом и адресом сервера.
    """
    sys.argv = ["streamlit", "run", "web.py", "--server.port=8501", "--server.address=0.0.0.0"]
    sys.exit(main(prog_name="streamlit"))
