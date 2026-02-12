#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для открытия index.html в браузере через локальный веб-сервер
"""
import webbrowser
import http.server
import socketserver
import threading
import time
from pathlib import Path

PORT = 5050

def start_server(directory):
    """Запускает локальный HTTP сервер"""
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    print(f"Сервер запущен на http://localhost:{PORT}")
    httpd.serve_forever()

def open_html_in_browser():
    # Получаем путь к index.html относительно этого скрипта
    script_dir = Path(__file__).parent
    html_file = script_dir / "index.html"
    
    # Проверяем существование файла
    if not html_file.exists():
        print(f"Ошибка: файл {html_file} не найден!")
        return
    
    # Запускаем сервер в отдельном потоке
    server_thread = threading.Thread(
        target=start_server,
        args=(str(script_dir),),
        daemon=True
    )
    server_thread.start()
    
    # Ждем немного, чтобы сервер успел запуститься
    time.sleep(1)
    
    # Открываем в браузере
    url = f"http://localhost:{PORT}/index.html"
    print(f"Открываю {html_file.name} в браузере...")
    print(f"URL: {url}")
    print("\nСервер работает. Нажмите Ctrl+C для остановки.")
    webbrowser.open(url)
    
    try:
        # Держим сервер запущенным
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nОстановка сервера...")

if __name__ == "__main__":
    import os
    open_html_in_browser()

