from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProductPage(BasePage):
    NOTEBOOK = (By.XPATH, '//*[@title="HP LP3065"]')
    WISHLIST_BUTTON = (By.XPATH, '//*[@class="fa-solid fa-heart"]')
    COMPARE_BUTTON = (By.XPATH, '//*[@class="fa-solid fa-arrow-right-arrow-left"]')
    PRODUCT_NAME = (By.XPATH, '//*[@id="product-info"]/ul/li[3]/a')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="button-cart"]')


    def click_notebook(self):
        self.assert_element(self.NOTEBOOK).click()

    def assert_wishlist_button_present(self):
        assert self.assert_element(self.WISHLIST_BUTTON)

    def assert_compare_button_present(self):
        assert self.assert_element(self.COMPARE_BUTTON)

    def assert_product_name(self, expected_name):
        name_notebook = self.assert_element(self.PRODUCT_NAME)
        assert name_notebook.get_attribute('text') == expected_name

    def assert_add_to_cart_button_present(self):
        assert self.assert_element(self.ADD_TO_CART_BUTTON)
