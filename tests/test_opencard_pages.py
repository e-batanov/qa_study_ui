import allure
from page_object.main_page import MainPage
from page_object.catalog_page import CatalogPage
from page_object.product_page import ProductPage
from page_object.login_admin_page import LoginAdminPage
from page_object.registration_page import RegistrationPage


@allure.story('Загрузка страниц')
@allure.title('Проверка работоспособности главной страницы')
def test_main_page(browser, url):
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.assert_logo_present()
    main_page.click_account()
    main_page.click_unauthenticated()

    if not main_page.is_unauthenticated_present():
        main_page.click_logout()

    main_page.click_cart()
    main_page.assert_empty_cart_message()


@allure.story('Загрузка страниц')
@allure.title('Проверка работоспособности страницы каталога')
def test_catalog_page(browser, url):
    catalog_page = CatalogPage(browser, f'{url}/en-gb/catalog/laptop-notebook')
    catalog_page.open()
    catalog_page.assert_breadcrumb_present()
    catalog_page.assert_category_title_present()
    catalog_page.assert_active_category()
    catalog_page.assert_product_list_present()
    catalog_page.assert_sort_dropdown_present()
    catalog_page.assert_limit_dropdown_present()


@allure.story('Загрузка страниц')
@allure.title('Проверка работоспособности страницы продукта')
def test_product_page(browser, url):
    product_page = ProductPage(browser, f'{url}/en-gb/catalog/laptop-notebook')
    product_page.open()
    product_page.click_notebook()
    product_page.assert_wishlist_button_present()
    product_page.assert_compare_button_present()
    product_page.assert_product_name("HP LP3065")
    product_page.assert_add_to_cart_button_present()


@allure.story('Загрузка страниц')
@allure.title('Проверка работоспособности страницы администратора')
def test_admin_page(browser, url):
    admin_page = LoginAdminPage(browser, f'{url}/administration')
    admin_page.open()
    admin_page.assert_login_prompt()
    admin_page.assert_username_field_present()
    admin_page.assert_password_field_present()
    admin_page.click_login()
    admin_page.assert_login_error_message()


@allure.story('Загрузка страниц')
@allure.title('Проверка работоспособности страницы регистрации')
def test_registration_customer(browser, url):
    registration_page = RegistrationPage(browser, f'{url}/index.php?route=account/register')
    registration_page.open()
    registration_page.assert_registration_form_present()
    registration_page.assert_firstname_field_present()
    registration_page.assert_lastname_field_present()
    registration_page.assert_email_field_present()
    registration_page.assert_password_field_present()
