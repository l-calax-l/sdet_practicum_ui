import allure
from pages.manager_page import ManagerPage
from tests.utils import generate_customer_data

@allure.title("TC-1: Успешное создание нового клиента")
@allure.description("Проверка полного цикла создания клиента с помощью Page Object.")
@allure.feature("Клиенты")
@allure.story("Создание клиента")
def test_add_customer(driver, base_url):
    # --- Инициализация Page Object ---
    manager_page = ManagerPage(driver, base_url)
    
    # --- Предусловие ---
    with allure.step("Открыть главную страницу менеджера"):
        manager_page.open()

    # --- Шаги теста ---
    manager_page.click_add_customer_button()
    
    first_name, post_code = generate_customer_data()
    last_name = "Testov"
    
    manager_page.fill_customer_form(first_name, last_name, post_code)
    
    alert_text = manager_page.accept_alert()
    with allure.step("Проверка текста в alert"):
        assert "Customer added successfully" in alert_text

    manager_page.go_to_customers_tab()
    manager_page.find_customer_by_name(first_name)
    
    # --- Проверка результата ---
    manager_page.verify_customer_data_in_table(first_name, last_name, post_code)