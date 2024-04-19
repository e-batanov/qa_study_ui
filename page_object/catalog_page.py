from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class CatalogPage(BasePage):
    BREADCRUMB = (By.XPATH, '//ul[@class = "breadcrumb"]')
    CATEGORY_TITLE = (By.XPATH, '//h2[text() = "Laptops & Notebooks"]')
    ACTIVE_CATEGORY = (By.XPATH, '//*[@class="list-group-item active"]')
    PRODUCT_LIST = (By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/form/div')
    SORT_DROPDOWN = (By.XPATH, '//select[@id = "input-sort"]')
    LIMIT_DROPDOWN = (By.XPATH, '//select[@id = "input-limit"]')
    LOGO = (By.XPATH, '//*[@id="logo"]')
    PRICE_NEW = (By.XPATH, '//*[@class="price-new"]')
    CURRENCY_CHANGE = (By.XPATH, '//*[@class="d-none d-md-inline"]')
    SELECTED_CURRENCY = (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')

    def get_prices(self):
        price_elements = self.browser.find_elements(*self.PRICE_NEW)
        prices = [element.text for element in price_elements]
        return prices

    def change_currency(self):
        self.assert_element(self.CURRENCY_CHANGE).click()
        self.assert_element(self.SELECTED_CURRENCY).click()

    def assert_breadcrumb_present(self):
        assert self.assert_element(self.BREADCRUMB)

    def assert_category_title_present(self):
        assert self.assert_element(self.CATEGORY_TITLE)

    def assert_active_category(self):
        assert self.assert_element(self.ACTIVE_CATEGORY)

    def assert_product_list_present(self):
        assert self.assert_element(self.PRODUCT_LIST)

    def assert_sort_dropdown_present(self):
        assert self.assert_element(self.SORT_DROPDOWN)

    def assert_limit_dropdown_present(self):
        assert self.assert_element(self.LIMIT_DROPDOWN)
