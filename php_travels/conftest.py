import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from php_travels.pages.login_page import Login
import allure
import time
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait




@pytest.fixture()
def setup_ch(request):
    # te akcje zostsaną wykonane przed testem:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/')
    driver.implicitly_wait(10)
    driver.maximize_window()
    wait = WebDriverWait(driver, 15, 1)
    request.cls.driver = driver
    request.cls.login_page = Login(driver)
    """It's easy - request.cls is the test class using the fixture, so request.cls.driver = ...
    is essentially the same as MyTestClass.driver = ... if MyTestClass uses the fixture.
    https://pytest.readthedocs.io/en/2.8.7/builtin.html"""
    before_failed = request.session.testsfailed

    # te akcje zostaną po wykonaniu akcji z plików z testami:
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    time.sleep(2)
    driver.quit()


@pytest.fixture()
def setup_ff(request):
    driver = webdriver.Firefox()
    driver.get('http://www.kurs-selenium.pl/demo/')
    driver.implicitly_wait(20)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.login_page = Login(driver)


    yield
    driver.quit()
