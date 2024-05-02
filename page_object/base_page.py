import inspect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step('Находим элемент по локатору {1}')
    def find_element(self, locator):
        return self.browser.find_element(*locator)

    @allure.step('Открываем URL: {1}')
    def open(self):
        self.browser.get(self.url)

    @allure.step('Нажимаем на элемент {1}')
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step('Вводим текст "{1}" в элемент {2}')
    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @property
    @allure.step('Получаем текущий URL')
    def current_url(self):
        return self.browser.current_url

    @allure.step('Ожидаем алерт')
    def alert(self, timeout=5):
        return WebDriverWait(self.browser, timeout).until(ec.alert_is_present())

    @allure.step('Проверяем элемент {1} с ожиданием {2}')
    def assert_element(
            self,
            locator,
            expected_condition=ec.visibility_of_element_located,
            timeout=5
    ):
        calling_method_name = inspect.currentframe().f_back.f_code.co_name
        self.logger.debug("Call function: %s", calling_method_name)
        self.logger.debug("%s работаю с элементом %s" % (self.class_name, str(locator)))
        try:
            return WebDriverWait(self.browser, timeout).until(expected_condition(locator))
        except TimeoutException:
            raise AssertionError(f'Не найден элемент [{locator}]')
