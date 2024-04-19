from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class AlertElement(BasePage):
    ALERT = By.XPATH, "//*[@class='alert alert-danger alert-dismissible']"
    CLOSE_ALERT = By.XPATH, "//*[@class='btn-close']"
    SUCCES_MODIFIED_PRODUCT = By.XPATH, "//*[text()=' Success: You have modified products! ']"

    def admin_alert(self):
        self.assert_element(self.ALERT)

    def close_alert(self):
        self.assert_element(self.CLOSE_ALERT).click()

    def check_succes_modified(self):
        self.assert_element(self.SUCCES_MODIFIED_PRODUCT)

    def alert_accept(self):
        self.alert().accept()
