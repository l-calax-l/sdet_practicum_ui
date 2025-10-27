import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
    options.add_argument("--window-size=1920,1080")

    # Автоматически скачиваем и устанавливаем подходящий ChromeDriver
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    # 'return' с продолжением
    yield browser

    # Закрываем браузер после теста
    browser.quit()
    
    