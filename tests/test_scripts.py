from tests.common import assert_element
from selenium.webdriver.common.by import By


def test_auth_admin(browser, url):
    browser.get(f'{url}/administration')

    assert_element(browser, (By.XPATH, '//*[@class="card"]'))
    user = browser.find_element(By.XPATH, '//*[@id="input-username"]')
    user.send_keys('user')
    password = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    password.send_keys('bitnami')
    browser.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    assert_element(browser, (By.XPATH, '//*[@id="nav-profile"]'))
    log_out = assert_element(browser, (By.XPATH, '//*[@id="nav-logout"]'))
    log_out.click()


def test_user_flow(browser, url):
    browser.get(url)

    assert_element(browser, (By.XPATH, '//*[@id="logo"]'))
    card_header = assert_element(browser, (By.XPATH, '//*[@id="header-cart"]'))
    card_header.click()
    card_header = browser.find_element(By.XPATH, "//*[text()='Your shopping cart is empty!']")

    card_header.click()
    add_to_cart_buttons = browser.find_element(By.XPATH, '//*[@class="fa-solid fa-shopping-cart"]')
    add_to_cart_buttons.click()

    card_header = assert_element(browser, (By.XPATH, '//*[@id="header-cart"]'))
    card_header.click()
    assert not card_header.text == 'Your shopping cart is empty!'


def test_check_main_price(browser, url):
    browser.get(url)

    assert_element(browser, (By.XPATH, '//*[@id="logo"]'))
    price_product_usa = browser.find_element(By.XPATH, '//*[@class="price-new"]').text
    browser.find_element(By.XPATH, '//*[@class="d-none d-md-inline"]').click()
    selected_currency = assert_element(browser, (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a'))
    selected_currency.click()
    price_product_eur = browser.find_element(By.XPATH, '//*[@class="price-new"]').text
    assert price_product_eur != price_product_usa


def test_check_catalog_price(browser, url):
    browser.get(f'{url}/en-gb/catalog/laptop-notebook')

    assert_element(browser, (By.XPATH, '//ul[@class = "breadcrumb"]'))
    price_product_usa = browser.find_element(By.XPATH, '//*[@class="price-new"]').text
    browser.find_element(By.XPATH, '//*[@class="d-none d-md-inline"]').click()
    selected_currency = assert_element(browser, (By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a'))
    selected_currency.click()
    price_product_str = browser.find_element(By.XPATH, '//*[@class="price-new"]').text
    assert price_product_str != price_product_usa
