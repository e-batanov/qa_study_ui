from tests.common import assert_element
from selenium.webdriver.common.by import By


def test_main_page(browser, url):
    browser.get(url)

    assert_element(browser, (By.XPATH, '//*[@id="logo"]'))
    account = assert_element(browser, (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div'))
    account.click()

    un_auth = assert_element(browser, (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[2]/a'))
    account.click()

    if not un_auth:
        browser.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[5]/a/span').click()

    card_header = assert_element(browser, (By.XPATH, '//*[@id="header-cart"]'))
    card_header.click()

    assert_element(browser, (By.XPATH, "//*[text()='Your shopping cart is empty!']"))


def test_catalog_page(browser, url):
    browser.get(f'{url}/en-gb/catalog/laptop-notebook')

    assert_element(browser, (By.XPATH, '//ul[@class = "breadcrumb"]'))
    browser.find_element(By.XPATH, '//h2[text() = "Laptops & Notebooks"]')
    browser.find_element(By.XPATH, '//*[@class="list-group-item active"]')
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/form/div')
    browser.find_element(By.XPATH, '//select[@id = "input-sort"]')
    browser.find_element(By.XPATH, '//select[@id = "input-limit"]')


def test_product_page(browser, url):
    browser.get(f'{url}/en-gb/catalog/laptop-notebook')

    notebook = assert_element(browser, (By.XPATH, '//*[@title="HP LP3065"]'))
    notebook.click()

    browser.find_element(By.XPATH, '//*[@class="fa-solid fa-heart"]')
    browser.find_element(By.XPATH, '//*[@class="fa-solid fa-arrow-right-arrow-left"]')
    name_notebook = browser.find_element(By.XPATH, '//*[@id="product-info"]/ul/li[3]/a')
    assert name_notebook.get_attribute('text') == "HP LP3065"
    browser.find_element(By.XPATH, '//*[@id = "button-cart"]')


def test_admin_page(browser, url):
    browser.get(f'{url}/administration')

    assert_element(browser, (By.XPATH, '//*[text() = " Please enter your login details."]'))
    browser.find_element(By.XPATH, '//*[@id="input-username"]')
    browser.find_element(By.XPATH, '//*[@id="input-password"]')
    btn_login = assert_element(browser, (By.XPATH, '//*[@class="btn btn-primary"]'))
    btn_login.click()
    assert_element(browser, (By.XPATH, '//*[text() = " No match for Username and/or Password. "]'))


def test_registration_customer(browser, url):
    browser.get(f'{url}/index.php?route=account/register')

    assert_element(browser, (By.XPATH, '//*[@id="form-register"]'))
    browser.find_element(By.XPATH, '//*[@id="input-firstname"]')
    browser.find_element(By.XPATH, '//*[@id="input-lastname"]')
    browser.find_element(By.XPATH, '//*[@id="input-email"]')
    browser.find_element(By.XPATH, '//*[@id="input-password"]')
    browser.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    assert_element(browser, (By.XPATH, '//*[text() = " Warning: You must agree to the Privacy Policy! "]'))
