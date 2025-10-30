from settings import DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    
    def __init__(self, driver, base_url, path):
        self.driver = driver
        self.base_url = base_url
        self.path = path
        self.url = f"{base_url}{path}"

    @allure.step("Открыть страницу")
    def open(self):
        """Открывает страницу по полному URL."""
        self.driver.get(self.url)
        allure.attach(
            self.url,
            name=f"Открыт URL: {self.path}",
            attachment_type=allure.attachment_type.URI_LIST
        )

    def find_element(self, locator, time=DEFAULT_TIMEOUT):
        """Находит один элемент, ожидая его появления."""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось найти элемент по локатору {locator}",
        )

    def find_elements(self, locator, time=DEFAULT_TIMEOUT):
        """Находит все элементы, ожидая их появления."""
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по локатору {locator}",
        )
    