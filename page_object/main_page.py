from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
import allure

class MainPage(BasePage):
    LOGO_OPENCARD = (By.XPATH, '//*[@id="logo"]')
    ACCOUNT = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div')
    UN_AUTH = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[2]/a')
    LOGOUT = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[5]/a/span')
    CART_HEADER = (By.XPATH, '//*[@id="header-cart"]')
    EMPTY_CART_MESSAGE = (By.XPATH, "//*[text()='Your shopping cart is empty!']")
    ADD_TO_CART_BUTTONS = (By.XPATH, '//*[@class="fa-solid fa-shopping-cart"]')
    PRICE_NEW = (By.XPATH, '//*[@class="price-new"]')
    CURRENCY_CHANGE = (By.XPATH, '//*[@class="d-none d-md-inline"]')
    SELECTED_CURRENCY = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')
    CARUSEL_BANNER_PRODUCT = By.ID, 'carousel-banner-0'
    CARUSEL_BANNER_ADVERTISING = By.XPATH, "//*[@id='carousel-banner-1']"
    ITEM_ADD = By.XPATH, '//*[@class="fa-solid fa-shopping-cart"]'
    PRICE = By.XPATH, "//*[@class='price']/span"
    CURRENCY = By.XPATH, "//*[text()='Currency']"
    CURRENCY_EURO = By.XPATH, "// *[text()='€ Euro']"
    CURRENCY_STERLING = By.XPATH, "// *[text()='£ Pound Sterling']"
    CURRENCY_DOLLAR = By.XPATH, "// *[text()='$ US Dollar']"

    @allure.step('Получаем цены продуктов')
    def get_prices(self):
        price_elements = self.browser.find_elements(*self.PRICE_NEW)
        prices = [element.text for element in price_elements]
        return prices

    @allure.step('Изменяем валюту')
    def change_currency(self):
        self.assert_element(self.CURRENCY_CHANGE).click()
        self.assert_element(self.SELECTED_CURRENCY).click()

    @allure.step('Нажимаем на корзину')
    def click_cart(self):
        self.assert_element(self.CART_HEADER).click()

    @allure.step('Проверяем наличие сообщения о пустой корзине')
    def assert_empty_cart_message(self):
        assert self.assert_element(self.EMPTY_CART_MESSAGE)

    @allure.step('Добавляем товар в корзину')
    def click_add_to_cart(self):
        self.assert_element(self.ADD_TO_CART_BUTTONS).click()

    @allure.step('Проверяем, что корзина не пуста')
    def assert_cart_not_empty(self):
        assert not self.assert_element(self.EMPTY_CART_MESSAGE)

    @allure.step('Проверяем наличие логотипа')
    def assert_logo_present(self):
        self.assert_element(self.LOGO_OPENCARD)

    @allure.step('Нажимаем на кнопку аккаунта')
    def click_account(self):
        self.assert_element(self.ACCOUNT).click()

    @allure.step('Нажимаем на кнопку неавторизованного пользователя')
    def click_unauthenticated(self):
        self.assert_element(self.UN_AUTH).click()

    @allure.step('Проверяем наличие кнопки неавторизованного пользователя')
    def is_unauthenticated_present(self):
        return self.browser.find_elements(*self.UN_AUTH)

    @allure.step('Выполняем выход из системы')
    def click_logout(self):
        self.assert_element(self.LOGOUT).click()

    @allure.step('Изменяем валюту на евро')
    def change_currency_to_eu(self):
        self.assert_element(self.CURRENCY).click()
        self.assert_element(self.CURRENCY_EURO).click()

    @allure.step('Изменяем валюту на фунты')
    def change_currency_to_ster(self):
        self.assert_element(self.CURRENCY).click()
        self.assert_element(self.CURRENCY_STERLING).click()

    @allure.step('Изменяем валюту на доллары')
    def change_currency_to_dol(self):
        self.assert_element(self.CURRENCY).click()
        self.assert_element(self.CURRENCY_DOLLAR).click()
