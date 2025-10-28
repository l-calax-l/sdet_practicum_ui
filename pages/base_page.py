from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Открывает страницу по URL."""
        self.driver.get(self.url)

    def find_element(self, locator, time=10):
        """Находит один элемент, ожидая его появления."""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}"
        )

    def find_elements(self, locator, time=10):
        """Находит все элементы, ожидая их появления."""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по локатору {locator}"
        )