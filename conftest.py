import pytest
import datetime
import os
import logging
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption('--headless', action='store_true')
    parser.addoption("--url", action="store", default="http://192.168.0.107:8081")
    parser.addoption("--log_level", default="INFO")
    parser.addoption('--executor')


if not os.path.exists("logs"):
    os.makedirs("logs")


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    executor = request.config.getoption('--executor')
    headless = request.config.getoption('--headless')

    driver = None
    options = None

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == 'chrome':
        options = ChromeOptions()

        if headless:
            options.add_argument('--headless=new')

        if executor is None:
            driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument('--headless')

        if executor is None:
            driver = webdriver.Firefox(options=options)

    else:
        driver = webdriver.Safari()

    caps = {
        "browserName": browser_name
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    if executor is not None:
        driver = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            options=options
        )

    driver.log_level = log_level
    driver.logger = logger
    Path('logs').mkdir(exist_ok=True)
    driver.test_name = request.node.name
    driver.maximize_window()

    request.addfinalizer(driver.quit)

    driver.url = url

    logger.info("Browser %s started" % browser)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s " % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
