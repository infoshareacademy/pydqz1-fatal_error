import time
import allure
import pytest
from allure_commons.types import AttachmentType
from php_travels.pages.login_page import Login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup_ch(request):
    # te akcje zostsaną wykonane przed testem:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/login')
    driver.implicitly_wait(10)
    driver.maximize_window()
    wait = WebDriverWait(driver, 15, 1)
    request.cls.driver = driver
    request.cls.login_page = Login(driver)
    before_failed = request.session.testsfailed
    # te akcje zostaną po wykonaniu akcji z plików z testami:
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    time.sleep(2)
    driver.quit()


@pytest.fixture()
def setup_ff(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/login')
    driver.implicitly_wait(10)
    driver.maximize_window()
    wait = WebDriverWait(driver, 15, 1)
    request.cls.driver = driver
    request.cls.login_page = Login(driver)
    yield
    driver.quit()
