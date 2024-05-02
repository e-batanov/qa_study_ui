import pytest
import datetime
import os
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.107:8081")
    parser.addoption("--log_level", default="INFO")


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

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromiumService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=FFOptions(), service=FFService())
    else:
        driver = webdriver.Safari()

    driver.log_level = log_level
    driver.logger = logger
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
