from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


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

    def check_firstname_field(self):
        self.assert_element(self.FIRSTNAME_FIELD)

    def input_firstname(self, firtsname):
        self.assert_element(self.FIRSTNAME_FIELD).send_keys(firtsname)

    def check_lastname_field(self):
        self.assert_element(self.LASTNAME_FIELD)

    def input_lastname(self, lastname):
        self.assert_element(self.LASTNAME_FIELD).send_keys(lastname)

    def check_email_field(self):
        self.assert_element(self.EMAIL_FIELD)

    def input_email(self, email):
        self.assert_element(self.EMAIL_FIELD).send_keys(email)

    def check_password_field(self):
        self.assert_element(self.PASSWORD_FIELD)

    def input_password(self, password):
        self.assert_element(self.PASSWORD_FIELD).send_keys(password)

    def check_submit_button(self):
        self.assert_element(self.SUBMIT_BUTTON)

    def click_submit_button(self):
        self.assert_element(self.SUBMIT_BUTTON).click()

    def click_checkbox_privaci_policy(self):
        self.assert_element(self.CHECKBOX).click()

    def click_continue_button(self):
        self.assert_element(self.CONTINUE_BUTTON, 1).click()

    def check_succes_registration(self):
        self.assert_element(self.SUCCESS_REGISTRATION)

    def assert_registration_form_present(self):
        assert self.assert_element(self.REGISTRATION_FORM)

    def assert_firstname_field_present(self):
        assert self.assert_element(self.FIRSTNAME_FIELD)

    def assert_lastname_field_present(self):
        assert self.assert_element(self.LASTNAME_FIELD)

    def assert_email_field_present(self):
        assert self.assert_element(self.EMAIL_FIELD)

    def assert_password_field_present(self):
        assert self.assert_element(self.PASSWORD_FIELD)

    def click_register(self):
        self.assert_element(self.REGISTER_BUTTON).click()

    def assert_privacy_policy_warning(self):
        assert self.assert_element(self.PRIVACY_POLICY_WARNING)
