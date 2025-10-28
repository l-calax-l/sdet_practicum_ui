from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .utils import generate_customer_data


def test_add_customer(driver, base_url):
    """Тест-кейс TC-1: Успешное создание нового клиента."""
    # Предусловие: URL из .env
    driver.get(base_url)

    # Нажать на кнопку "Add Customer"
    add_customer_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='addCust()']"))
    )
    add_customer_btn.click()

    # Сгенерировать тестовые данные
    first_name, post_code = generate_customer_data()
    last_name = "Testov"

    # Ввод данных

    # Ждем, пока поле "First Name" не станет видимым
    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[ng-model='fName']"))
    )
    first_name_input.send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR, "input[ng-model='lName']").send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, "input[ng-model='postCd']").send_keys(post_code)

    # Нажать кнопку "Add Customer" под формой
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Принять alert ---
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    assert "Customer added successfully" in alert.text
    alert.accept()

    # Перейти на вкладку "Customers"
    driver.find_element(By.CSS_SELECTOR, "button[ng-click='showCust()']").click()

    # Найти созданного клиента
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[ng-model='searchCustomer']"))
    )
    search_input.send_keys(first_name)

    # Ожидаемый результат: Проверяем данные в таблице
    first_name_cell = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    last_name_cell = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(2)")
    post_code_cell = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(3)")

    assert first_name_cell.text == first_name
    assert last_name_cell.text == last_name
    assert post_code_cell.text == post_code

