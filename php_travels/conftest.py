import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.page_one import SearchFeature
import time
import allure
from allure_commons.types import AttachmentType


@pytest.fixture()
def setup_ch(request):
    # te akcje zostsaną wykonane przed testem:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.search_feature = SearchFeature(driver)
    before_failed = request.session.testsfailed
    # te akcje zostaną po wykonaniu akcji z plików z testami:
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    time.sleep(2)
    driver.quit()


# @pytest.fixture()
# def setup_ff(request):
#     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     driver.get('http://www.kurs-selenium.pl/demo/')
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     request.cls.driver = driver
#     request.cls.search_feature = SearchFeature(driver)
#     yield
#     driver.quit()
