from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
import allure


class RegistrationPage(BasePage):
    REGISTRATION_FORM = (By.XPATH, '//*[@id="form-register"]')
    FIRSTNAME_FIELD = (By.XPATH, '//*[@id="input-firstname"]')
    LASTNAME_FIELD = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="input-email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="input-password"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@class="btn btn-primary"]')
    PRIVACY_POLICY_WARNING = (By.XPATH, '//*[text() = " Warning: You must agree to the Privacy Policy! "]')
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
    CHECKBOX = By.XPATH, "//*[@name='agree']"
    CONTINUE_BUTTON = By.XPATH, "//*[@class='btn btn-primary']"
    SUCCESS_REGISTRATION = By.XPATH, "//h1[text()='Your Account Has Been Created!']"
    MY_ACCOUNT = By.XPATH, "//*[@class='fa-solid fa-user']"

    @allure.step('Проверяем наличие поля имени')
    def check_firstname_field(self):
        self.assert_element(self.FIRSTNAME_FIELD)

    @allure.step('Вводим имя "{1}"')
    def input_firstname(self, firstname):
        self.assert_element(self.FIRSTNAME_FIELD).send_keys(firstname)

    @allure.step('Проверяем наличие поля фамилии')
    def check_lastname_field(self):
        self.assert_element(self.LASTNAME_FIELD)

    @allure.step('Вводим фамилию "{1}"')
    def input_lastname(self, lastname):
        self.assert_element(self.LASTNAME_FIELD).send_keys(lastname)

    @allure.step('Проверяем наличие поля электронной почты')
    def check_email_field(self):
        self.assert_element(self.EMAIL_FIELD)

    @allure.step('Вводим электронную почту "{1}"')
    def input_email(self, email):
        self.assert_element(self.EMAIL_FIELD).send_keys(email)

    @allure.step('Проверяем наличие поля пароля')
    def check_password_field(self):
        self.assert_element(self.PASSWORD_FIELD)

    @allure.step('Вводим пароль "{1}"')
    def input_password(self, password):
        self.assert_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step('Проверяем наличие кнопки отправки')
    def check_submit_button(self):
        self.assert_element(self.SUBMIT_BUTTON)

    @allure.step('Нажимаем на кнопку отправки')
    def click_submit_button(self):
        self.assert_element(self.SUBMIT_BUTTON).click()

    @allure.step('Нажимаем на чекбокс политики конфиденциальности')
    def click_checkbox_privacy_policy(self):
        self.assert_element(self.CHECKBOX).click()

    @allure.step('Нажимаем на кнопку продолжения')
    def click_continue_button(self):
        self.assert_element(self.CONTINUE_BUTTON, 1).click()

    @allure.step('Проверяем успешную регистрацию')
    def check_success_registration(self):
        self.assert_element(self.SUCCESS_REGISTRATION)

    @allure.step('Проверяем наличие формы регистрации')
    def assert_registration_form_present(self):
        assert self.assert_element(self.REGISTRATION_FORM)

    @allure.step('Проверяем наличие поля имени')
    def assert_firstname_field_present(self):
        assert self.assert_element(self.FIRSTNAME_FIELD)

    @allure.step('Проверяем наличие поля фамилии')
    def assert_lastname_field_present(self):
        assert self.assert_element(self.LASTNAME_FIELD)

    @allure.step('Проверяем наличие поля электронной почты')
    def assert_email_field_present(self):
        assert self.assert_element(self.EMAIL_FIELD)

    @allure.step('Проверяем наличие поля пароля')
    def assert_password_field_present(self):
        assert self.assert_element(self.PASSWORD_FIELD)

    @allure.step('Нажимаем на кнопку регистрации')
    def click_register(self):
        self.assert_element(self.REGISTER_BUTTON).click()

    @allure.step('Проверяем наличие предупреждения о политике конфиденциальности')
    def assert_privacy_policy_warning(self):
        assert self.assert_element(self.PRIVACY_POLICY_WARNING)
