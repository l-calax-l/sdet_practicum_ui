import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ManagerPageLocators


class ManagerPage(BasePage):
    path = "/angularJs-protractor/BankingProject/#/manager"
    
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url, self.path)

    @allure.step("Нажать на кнопку 'Add Customer'")
    def click_add_customer_button(self):
        self.find_element(ManagerPageLocators.ADD_CUSTOMER_BUTTON).click()

    @allure.step(
        "Заполнить форму клиента: Имя={first_name}, "
        "Фамилия={last_name}, Индекс={post_code}"
    )
    def fill_customer_form(self, first_name, last_name, post_code):
        self.find_element(ManagerPageLocators.FIRST_NAME_INPUT).send_keys(
            first_name
        )  # noqa: E501
        self.find_element(ManagerPageLocators.LAST_NAME_INPUT).send_keys(
            last_name
        )  # noqa: E501
        self.find_element(ManagerPageLocators.POST_CODE_INPUT).send_keys(
            post_code
        )  # noqa: E501
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
        self.find_element(ManagerPageLocators.SEARCH_INPUT).send_keys(
            first_name
        )  # noqa: E501
        # Ожидаем, что таблица отфильтруется и будет видна
        self.find_element(ManagerPageLocators.CUSTOMERS_TABLE)

    @allure.step("Проверить данные клиента в таблице")
    def verify_customer_data_in_table(self, first_name, last_name, post_code):
        first_name_cell_text = self.find_element(
            ManagerPageLocators.ALL_FIRST_NAME_CELLS
        ).text
        last_name_cell_text = self.find_element(
            ManagerPageLocators.ALL_LAST_NAME_CELLS
        ).text
        post_code_cell_text = self.find_element(
            ManagerPageLocators.ALL_POST_CODE_CELLS
        ).text

        with allure.step(
            f"Проверка имени: ожидаем '{first_name}', "
            f"в таблице '{first_name_cell_text}'"
        ):
            assert first_name_cell_text == first_name

        with allure.step(
            f"Проверка фамилии: ожидаем '{last_name}', "
            f"в таблице '{last_name_cell_text}'"
        ):
            assert last_name_cell_text == last_name

        with allure.step(
            f"Проверка индекса: ожидаем '{post_code}', "
            f"в таблице '{post_code_cell_text}'"
        ):
            assert post_code_cell_text == post_code

    @allure.step("Нажать на заголовок 'First Name' для сортировки")
    def sort_by_first_name(self):
        self.find_element(ManagerPageLocators.FIRST_NAME_HEADER).click()

    @allure.step("Получить список имен клиентов из таблицы")
    def get_customer_first_names(self):
        # Ожидаем, что таблица будет видна
        self.find_element(ManagerPageLocators.CUSTOMERS_TABLE)
        name_cells = self.find_elements(
            ManagerPageLocators.ALL_FIRST_NAME_CELLS
        )  # noqa: E501
        return [cell.text for cell in name_cells]

    @allure.step("Удалить клиента с именем: {customer_name}")
    def delete_customer(self, customer_name):
        # Используем динамический локатор
        customer_row = self.find_element(
            ManagerPageLocators.customer_row_by_text(customer_name)
        )
        # Внутри строки ищем кнопку Delete
        delete_btn = customer_row.find_element(
            By.CSS_SELECTOR, "button[ng-click^='deleteCust']"
        )
        delete_btn.click()
        