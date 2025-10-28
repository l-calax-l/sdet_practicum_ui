import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .utils import generate_customer_data


def test_add_customer(driver, base_url):
    """Тест-кейс TC-1: Успешное создание нового клиента."""
    # Предусловие: URL из .env
    driver.get(base_url)

@allure.step("Нажать на кнопку 'Add Customer'")
def step_click_add_customer_button(driver):
    add_customer_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='addCust()']"))
    )
    add_customer_btn.click()

@allure.step("Заполнить форму клиента: Имя={first_name}, Фамилия={last_name}, Индекс={post_code}")
def step_fill_customer_form(driver, first_name, last_name, post_code):
    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[ng-model='fName']"))
    )
    first_name_input.send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR, "input[ng-model='lName']").send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, "input[ng-model='postCd']").send_keys(post_code)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@allure.step("Принять alert после добавления клиента")
def step_accept_alert(driver):
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    return alert_text

@allure.step("Перейти на вкладку 'Customers' и найти клиента по имени: {first_name}")
def step_find_customer_by_name(driver, first_name):
    driver.find_element(By.CSS_SELECTOR, "button[ng-click='showCust()']").click()
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[ng-model='searchCustomer']"))
    )
    search_input.send_keys(first_name)

@allure.step("Проверить, что данные клиента в таблице соответствуют ожидаемым")
def step_verify_customer_data_in_table(driver, first_name, last_name, post_code):
    first_name_cell = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    last_name_cell = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
    post_code_cell = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(3)")

    with allure.step(f"Проверка имени: ожидаем '{first_name}', в таблице '{first_name_cell.text}'"):
        assert first_name_cell.text == first_name
    with allure.step(f"Проверка фамилии: ожидаем '{last_name}', в таблице '{last_name_cell.text}'"):
        assert last_name_cell.text == last_name
    with allure.step(f"Проверка индекса: ожидаем '{post_code}', в таблице '{post_code_cell.text}'"):
        assert post_code_cell.text == post_code

@allure.title("TC-1: Успешное создание нового клиента")
@allure.description("Проверка полного цикла создания нового клиента с динамическими данными и валидация его наличия в таблице.")
@allure.feature("Клиенты")
@allure.story("Создание клиента")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_customer(driver, base_url):
    
    with allure.step("Предусловие: Открыть главную страницу"):
        driver.get(base_url)

    step_click_add_customer_button(driver)

    first_name, post_code = generate_customer_data()
    last_name = "Testov"
    
    step_fill_customer_form(driver, first_name, last_name, post_code)
    
    alert_text = step_accept_alert(driver)
    with allure.step("Проверка текста в alert"):
        assert "Customer added successfully" in alert_text

    step_find_customer_by_name(driver, first_name)
    
    step_verify_customer_data_in_table(driver, first_name, last_name, post_code)
