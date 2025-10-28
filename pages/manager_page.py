import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ManagerPageLocators:
    # --- Локаторы кнопок-вкладок ---
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    CUSTOMERS_BUTTON = (By.CSS_SELECTOR, "button[ng-click='showCust()']")

    # --- Локаторы полей формы Add Customer ---
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # --- Локаторы на вкладке Customers ---
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[ng-model='searchCustomer']")
    CUSTOMERS_TABLE_BODY = (By.CSS_SELECTOR, "tbody")
    FIRST_NAME_CELL = (By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    LAST_NAME_CELL = (By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
    POST_CODE_CELL = (By.CSS_SELECTOR, "tbody tr td:nth-child(3)")

    # --- Локаторы для сортировки ---
    FIRST_NAME_HEADER = (By.CSS_SELECTOR, "a[ng-click*='fName']")

class ManagerPage(BasePage):
    @allure.step("Нажать на кнопку 'Add Customer'")
    def click_add_customer_button(self):
        self.find_element(ManagerPageLocators.ADD_CUSTOMER_BUTTON).click()

    @allure.step("Заполнить форму клиента: Имя={first_name}, Фамилия={last_name}, Индекс={post_code}")
    def fill_customer_form(self, first_name, last_name, post_code):
        self.find_element(ManagerPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(ManagerPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(ManagerPageLocators.POST_CODE_INPUT).send_keys(post_code)
        self.find_element(ManagerPageLocators.SUBMIT_CUSTOMER_BUTTON).click()

    @allure.step("Принять alert после добавления клиента")
    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    @allure.step("Перейти на вкладку 'Customers'")
    def go_to_customers_tab(self):
        self.find_element(ManagerPageLocators.CUSTOMERS_BUTTON).click()

    @allure.step("Найти клиента по имени: {first_name}")
    def find_customer_by_name(self, first_name):
        self.find_element(ManagerPageLocators.SEARCH_INPUT).send_keys(first_name)
        # Ожидаем, что таблица загрузится
        self.find_element(ManagerPageLocators.CUSTOMERS_TABLE_BODY)

    @allure.step("Проверить, что данные клиента в таблице соответствуют ожидаемым")
    def verify_customer_data_in_table(self, first_name, last_name, post_code):
        first_name_cell_text = self.find_element(ManagerPageLocators.FIRST_NAME_CELL).text
        last_name_cell_text = self.find_element(ManagerPageLocators.LAST_NAME_CELL).text
        post_code_cell_text = self.find_element(ManagerPageLocators.POST_CODE_CELL).text

        with allure.step(f"Проверка имени: ожидаем '{first_name}', в таблице '{first_name_cell_text}'"):
            assert first_name_cell_text == first_name
        with allure.step(f"Проверка фамилии: ожидаем '{last_name}', в таблице '{last_name_cell_text}'"):
            assert last_name_cell_text == last_name
        with allure.step(f"Проверка индекса: ожидаем '{post_code}', в таблице '{post_code_cell_text}'"):
            assert post_code_cell_text == post_code
    
    @allure.step("Нажать на заголовок 'First Name' для сортировки")
    def sort_by_first_name(self):
        self.find_element(ManagerPageLocators.FIRST_NAME_HEADER).click()

    @allure.step("Получить список имен клиентов из таблицы")
    def get_customer_first_names(self):
        # Ждем, пока таблица загрузится
        self.find_element(ManagerPageLocators.CUSTOMERS_TABLE_BODY)
        # Находим все ячейки с именами
        name_cells = self.find_elements(ManagerPageLocators.FIRST_NAME_CELL)
        # Возвращаем список текстовых значений этих ячеек
        return [cell.text for cell in name_cells]
    
    @allure.step("Удалить клиента с именем: {customer_name}")
    def delete_customer(self, customer_name):
        # Находим строку по тексту имени, поднимаемся к родителю (tr)
        customer_row = self.find_element((By.XPATH, f"//td[text()='{customer_name}']/.."))
        # Внутри строки ищем кнопку Delete
        delete_btn = customer_row.find_element(By.CSS_SELECTOR, "button[ng-click^='deleteCust']")
        delete_btn.click()
    