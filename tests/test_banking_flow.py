import allure
from settings import DEFAULT_LAST_NAME
from pages.manager_page import ManagerPage
from tests.utils import generate_customer_data
from tests.utils import find_customer_to_delete


@allure.title("TC-1: Успешное создание нового клиента")
@allure.description("Создание и проверка нового клиента через POM.")
@allure.feature("Клиенты")
@allure.story("Создание клиента")
def test_add_customer(driver, base_url):
    manager_page = ManagerPage(driver, base_url)

    manager_page.open()

    manager_page.click_add_customer_button()

    first_name, post_code = generate_customer_data()
    last_name = DEFAULT_LAST_NAME

    manager_page.fill_customer_form(first_name, last_name, post_code)
    manager_page.submit_customer_form()
    
    alert_text = manager_page.accept_alert()
    with allure.step("Проверка текста в alert"):
        assert "Customer added successfully" in alert_text

    manager_page.go_to_customers_tab()
    manager_page.find_customer_by_name(first_name)

    with allure.step("Проверить, что данные клиента в таблице соответствуют ожидаемым"):
        customer_data = manager_page.get_customer_data_from_row()

        assert customer_data["first_name"] == first_name
        assert customer_data["last_name"] == last_name
        assert customer_data["post_code"] == post_code


@allure.title("TC-2: Сортировка клиентов по имени")
@allure.feature("Клиенты")
@allure.story("Сортировка")
def test_sort_customers_by_first_name(driver, base_url):
    manager_page = ManagerPage(driver, base_url)

    manager_page.open()
    manager_page.go_to_customers_tab()

    with allure.step("Получить оригинальный список имен"):
        original_names = manager_page.get_customer_first_names()
        # Убедимся, что имена есть в таблице
        assert len(original_names) > 0, "Нет клиентов для сортировки"

    with allure.step("Отсортировать по убыванию (Z-A) и проверить"):
        manager_page.sort_by_first_name()
        sorted_names_desc = manager_page.get_customer_first_names()
        assert sorted_names_desc == sorted(
            original_names, reverse=True
        ), "Сортировка по убыванию не работает"

    with allure.step("Отсортировать по возрастанию (A-Z) и проверить"):
        manager_page.sort_by_first_name()
        sorted_names_asc = manager_page.get_customer_first_names()
        assert sorted_names_asc == sorted(
            original_names
        ), "Сортировка по возрастанию не работает"


@allure.title("TC-3: Удаление клиента")
@allure.feature("Клиенты")
@allure.story("Удаление")
def test_delete_customer(driver, base_url):
    manager_page = ManagerPage(driver, base_url)
    
    manager_page.open()
    manager_page.go_to_customers_tab()

    with allure.step("Найти клиента для удаления"):
        all_names = manager_page.get_customer_first_names()
        assert len(all_names) > 0, "Нет клиентов для удаления"
        name_to_delete = find_customer_to_delete(all_names)

    with allure.step(f"Удалить клиента '{name_to_delete}' и проверить"):
        manager_page.delete_customer(name_to_delete)
        remaining_names = manager_page.get_customer_first_names()
        assert (
            name_to_delete not in remaining_names
        ), f"Клиент '{name_to_delete}' не был удален из таблицы"
