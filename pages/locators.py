from selenium.webdriver.common.by import By


class ManagerPageLocators:
    """Хранит все локаторы для страницы Manager."""

    # Кнопки-вкладки
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR, "button[ng-click='showCust()']")

    # Форма Add Customer
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Элементы на вкладке Customers
    CUSTOMERS_TABLE = (By.CSS_SELECTOR, "table.table-striped")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[ng-model='searchCustomer']")

    # Обобщенные локаторы для ВСЕХ ячеек в столбцах
    ALL_FIRST_NAME_CELLS = (By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    ALL_LAST_NAME_CELLS = (By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
    ALL_POST_CODE_CELLS = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")

    # Элементы для сортировки
    FIRST_NAME_HEADER = (By.CSS_SELECTOR, "a[ng-click*='fName']")

    # Динамический локатор
    @staticmethod
    def customer_row_by_text(text):
        """Возвращает локатор для строки таблицы по тексту внутри нее."""
        return By.XPATH, f"//tr[contains(., '{text}')]"
