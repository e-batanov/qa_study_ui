from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def open(self):
        self.browser.get(self.url)

    def click(self, locator):
        self.find_element(locator).click()

    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @property
    def current_url(self):
        return self.browser.current_url

    def alert(self, timeout=5):
        return WebDriverWait(self.browser, timeout).until(ec.alert_is_present())

    def assert_element(
            self,
            locator,
            expected_condition=ec.visibility_of_element_located,
            timeout=5
    ):
        try:
            return WebDriverWait(self.browser, timeout).until(expected_condition(locator))
        except TimeoutException:
            raise AssertionError(f'Не найден элемент [{locator}]')
