import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """
    Фикстура, которая читает и возвращает базовый URL для тестов
    из переменной окружения BASE_URL.
    """
    url = os.getenv("BASE_URL")
    if not url:
        pytest.fail("Переменная окружения BASE_URL не задана в .env файле")
    return url


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для подготовки и закрытия браузера перед/после каждого теста.
    Автоматически управляет версией ChromeDriver.
    """
    options = webdriver.ChromeOptions()

    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless")
        
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-proxy-server")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()
