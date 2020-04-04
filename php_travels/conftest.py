import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/')
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()


@pytest.fixture()
def setup1(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/register')
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.register_page = RegisterPage(driver)
    request.cls.account_page = AccountPage(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()