import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import Login_Page

@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level teardown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running method level setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = Login_Page(driver)
    lp.login("Nithya dhanapal", "nithyadhanapal@yahoo.com")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")