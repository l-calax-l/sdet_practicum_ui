import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Загружаем переменные из .env файла в окружение проекта
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """
    Фикстура, которая читает и возвращает базовый URL для тестов
    из переменной окружения BASE_URL.
    """
    url = os.getenv("BASE_URL")
    if not url:
        # Если переменная не найдена, тесты должны упасть с понятной ошибкой
        pytest.fail("Переменная окружения BASE_URL не задана в .env файле")
    return url

@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для подготовки и закрытия браузера перед/после каждого теста.
    Автоматически управляет версией ChromeDriver.
    """
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Раскомментировать для запуска в CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-proxy-server")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)

    # 'return' с продолжением
    yield browser

    # Закрываем браузер после теста
    browser.quit()
