from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminPage(BasePage):
    TITLE = By.XPATH, "//*[text()='Administration']"
    USERNAME_FIELD = By.XPATH, "//*[@id='input-username']"
    PASSWORD_FIELD = By.XPATH, "//*[@id='input-password']"
    LOGIN_BUTTON = By.XPATH, "//*[@type='submit']"
    LOGOUT = By.XPATH, "//*[@id='nav-logout']/a/span"

    NAVIGATION_CATALOG = By.XPATH, "//*[@id='menu-catalog']"
    CATALOG_PRODUCTS = By.XPATH, "//*[text()='Products']"
    ADD_NEW = By.XPATH, "//div[@class='float-end']/a[@class='btn btn-primary']"
    PRODUCT_NAME_INPUT = By.XPATH, "//*[@placeholder='Product Name']"
    META_TAG_TITLE_INPUT = By.XPATH, "//*[@placeholder='Meta Tag Title']"
    DATA_ADD_PRODUCT = By.XPATH, "//*[text()='Data']"
    MODEL = By.XPATH, "//*[@placeholder='Model']"
    SEO = By.XPATH, "//*[text()='SEO']"
    SEO_KEYWORD = By.XPATH, "//*[@placeholder='Keyword']"
    SAVE_BUTTON = By.XPATH, "//*[@class='fa-solid fa-floppy-disk']"
    FILTER_BUTTON = By.XPATH, "//*[@id='button-filter']"
    CHECKBOX = By.XPATH, "//*[@type='checkbox' and @name='selected[]']"
    DELETE_PRODUCT = By.XPATH, "//*[@class='btn btn-danger']"

    @allure.step('Выбираем кнопку каталога')
    def choose_catalog(self):
        self.assert_element(self.NAVIGATION_CATALOG).click()

    @allure.step('Выбираем продукт')
    def choose_products(self):
        self.assert_element(self.CATALOG_PRODUCTS).click()

    @allure.step('Добавляем новый продукт')
    def add_new_product(self):
        self.assert_element(self.ADD_NEW).click()

    @allure.step('Вводим имя продукта')
    def input_product_name(self, name):
        self.assert_element(self.PRODUCT_NAME_INPUT).send_keys(name)

    @allure.step('Вводим мета-тег')
    def input_meta_tag(self, meta_tag):
        self.assert_element(self.META_TAG_TITLE_INPUT).send_keys(meta_tag)

    @allure.step('Вводим информацию о продукте')
    def choose_data(self):
        self.assert_element(self.DATA_ADD_PRODUCT).click()

    @allure.step('Вводим модель продукта')
    def input_model(self, model):
        self.assert_element(self.MODEL).send_keys(model)

    @allure.step('Выбираем SEO')
    def choose_seo(self):
        self.assert_element(self.SEO).click()

    @allure.step('Вводим SEO ключевое слово')
    def input_seo_keyword(self, keyword):
        self.assert_element(self.SEO_KEYWORD).send_keys(keyword)

    @allure.step('Сохраняем продукт')
    def save_product(self):
        self.assert_element(self.SAVE_BUTTON).click()

    @allure.step('Применяем фильтр')
    def apply_filter(self):
        self.assert_element(self.FILTER_BUTTON).click()

    @allure.step('Кликаем на чекбокс')
    def click_checkbox(self):
        self.assert_element(self.CHECKBOX).click()

    @allure.step('Удаляем продукт')
    def delete_product(self):
        self.assert_element(self.DELETE_PRODUCT).click()

    @allure.step('Проверяем поле ввода имени пользователя')
    def check_username_field(self):
        self.assert_element(self.USERNAME_FIELD)

    @allure.step('Проверяем поле ввода пароля')
    def check_password_field(self):
        self.assert_element(self.PASSWORD_FIELD)

    @allure.step('Проверяем кнопку входа')
    def check_login_button(self):
        self.assert_element(self.LOGIN_BUTTON)

    @allure.step('Кликаем на кнопку входа')
    def click_login_button(self):
        self.assert_element(self.LOGIN_BUTTON).click()

    @allure.step('Выполняем вход в систему')
    def login(self, username, password):
        self.assert_element(self.USERNAME_FIELD).send_keys(username)
        self.assert_element(self.PASSWORD_FIELD).send_keys(password)
        self.assert_element(self.LOGIN_BUTTON).click()

    @allure.step('Проверяем текст кнопки выхода')
    def logout_text(self):
        self.assert_element(self.LOGOUT)
