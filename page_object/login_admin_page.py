from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class LoginAdminPage(BasePage):
    LOGIN_PROMPT = (By.XPATH, '//*[text() = " Please enter your login details."]')
    USERNAME_FIELD = (By.XPATH, '//*[@id="input-username"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="input-password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@class="btn btn-primary"]')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//*[text() = " No match for Username and/or Password. "]')
    CARD = (By.XPATH, '//*[@class="card"]')
    NAV_PROFILE = (By.XPATH, '//*[@id="nav-profile"]')
    NAV_LOGOUT = (By.XPATH, '//*[@id="nav-logout"]')
    CATALOG_TAB = (By.XPATH, '//li[@id = "menu-catalog"]/a')
    PRODUCTS_TAB = (By.XPATH, '//li[@id = "menu-catalog"]//a[text() = "Products"]')
    ADD_PRODUCT_BUTTON = (By.XPATH, '//a[@data-original-title = "Add New"]')
    DELETE_PRODUCT_BUTTON = (By.XPATH, '//button[@data-original-title = "Delete"]')
    PRODUCT_NAME_INPUT = (By.XPATH, '//input[@id  = "input-name1"]')
    META_TAG_INPUT = (By.XPATH, '//input[@id  = "input-meta-title1"]')
    DATA_TAB = (By.XPATH, '//a[@data-toggle = "tab"][text() = "Data"]')
    MODEL_INPUT = (By.XPATH, '//input[@id = "input-model"]')
    PRICE_INPUT = (By.XPATH, '//input[@id = "input-price"]')
    SAVE_BUTTON = (By.XPATH, '//button[@data-original-title = "Save"]')
    PRODUCT_NAME_FILTER_INPUT = (By.XPATH, '//input[@id = "input-name"]')
    FILTER_BUTTON = (By.XPATH, '//button[@id = "button-filter"]')

    PRODUCT_LIST = (By.XPATH, '//table')
    NEW_PRODUCT = (By.XPATH, '//table/tbody/tr[1]')
    PRODUCT_CHECKBOX = (By.XPATH, './td[1]/input')
    PRODUCT_NAME = (By.XPATH, './td[3]')
    PRODUCT_MODEL = (By.XPATH, './td[4]')
    PRODUCT_PRICE = (By.XPATH, './td[5]')

    def login(self, username, password):
        self.assert_element(self.USERNAME_FIELD).send_keys(username)
        self.assert_element(self.PASSWORD_FIELD).send_keys(password)
        self.assert_element(self.LOGIN_BUTTON).click()

    def assert_profile_present(self):
        assert self.assert_element(self.NAV_PROFILE)

    def click_logout(self):
        self.assert_element(self.NAV_LOGOUT).click()

    def assert_login_prompt(self):
        assert self.assert_element(self.LOGIN_PROMPT)

    def assert_username_field_present(self):
        assert self.assert_element(self.USERNAME_FIELD)

    def assert_password_field_present(self):
        assert self.assert_element(self.PASSWORD_FIELD)

    def click_login(self):
        self.assert_element(self.LOGIN_BUTTON).click()

    def assert_login_error_message(self):
        assert self.assert_element(self.LOGIN_ERROR_MESSAGE)
