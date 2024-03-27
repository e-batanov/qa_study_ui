from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def assert_element(
        driver,
        locator,
        expected_condition=ec.visibility_of_element_located,
        timeout=5
):
    try:
        return WebDriverWait(driver, timeout).until(expected_condition(locator))
    except TimeoutException:
        raise AssertionError(f'Не найден элемент [{locator}]')
