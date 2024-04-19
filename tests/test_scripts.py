import time

from page_object.login_admin_page import LoginAdminPage
from page_object.main_page import MainPage
from page_object.catalog_page import CatalogPage
from page_object.admin_page import AdminPage
from page_object.alert_element import AlertElement
from page_object.base_page import BasePage
from page_object.registration_page import RegistrationPage


def test_auth_admin(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/administration')
    login_admin_page.open()
    login_admin_page.assert_element(login_admin_page.CARD)
    login_admin_page.login('user', 'bitnami')
    login_admin_page.assert_profile_present()
    login_admin_page.click_logout()


def test_user_flow(browser, url):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.assert_element(main_page.LOGO_OPENCARD)
    main_page.click_cart()
    main_page.assert_empty_cart_message()
    main_page.click_add_to_cart()
    main_page.click_cart()
    main_page.assert_cart_not_empty()


def test_check_main_price(browser, url):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.assert_element(main_page.LOGO_OPENCARD)
    prices_usa = main_page.get_prices()
    main_page.change_currency()
    prices_eur = main_page.get_prices()
    assert prices_eur != prices_usa, 'Валюта не изменилась'


def test_check_catalog_price(browser, url):
    catalog_page = CatalogPage(browser, f'{url}/en-gb/catalog/laptop-notebook')
    catalog_page.open()
    catalog_page.assert_element(catalog_page.BREADCRUMB)
    prices_usa = catalog_page.get_prices()
    catalog_page.change_currency()
    prices_str = catalog_page.get_prices()
    assert prices_str != prices_usa, 'Валюта не изменилась'


def test_add_product(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/administration')
    login_admin_page.open()
    login_admin_page.assert_element(login_admin_page.CARD)
    login_admin_page.login('user', 'bitnami')
    login_admin_page.assert_profile_present()

    admin_page = AdminPage(browser, BasePage.current_url)
    admin_page.choose_catalog()
    admin_page.choose_products()
    admin_page.add_new_product()
    admin_page.input_product_name("test")
    admin_page.input_meta_tag("test")
    admin_page.choose_data()
    admin_page.input_model("test")
    admin_page.choose_seo()
    admin_page.input_seo_keyword("test")
    admin_page.save_product()
    alert_element = AlertElement(browser, BasePage.current_url)
    alert_element.check_succes_modified()


def test_del_product(browser, url):
    login_admin_page = LoginAdminPage(browser, f'{url}/administration')
    login_admin_page.open()
    login_admin_page.assert_element(login_admin_page.CARD)
    login_admin_page.login('user', 'bitnami')
    login_admin_page.assert_profile_present()

    admin_page = AdminPage(browser, BasePage.current_url)
    admin_page.choose_catalog()
    admin_page.choose_products()
    admin_page.input_product_name("test")
    admin_page.apply_filter()
    admin_page.click_checkbox()
    admin_page.delete_product()

    alert_element = AlertElement(browser, BasePage.current_url)
    alert_element.alert_accept()
    alert_element.check_succes_modified()


def test_register_user(browser, url):
    browser.get(url + "/en-gb?route=account/register")

    registration_page = RegistrationPage(browser, BasePage.current_url)
    registration_page.input_firstname("test")
    registration_page.input_lastname("test")
    registration_page.input_email("test@test.test")
    registration_page.input_password("test")
    registration_page.click_checkbox_privaci_policy()
    registration_page.click_continue_button()
    registration_page.check_succes_registration()


def test_change_currency(browser, url):
    main_page = MainPage(browser, url)
    main_page.change_currency_to_eu()
    main_page.change_currency_to_ster()
    main_page.change_currency_to_dol()
