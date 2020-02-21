import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType


@pytest.fixture()
def setup(request):
# te akcje zostaną wykonane przed testem:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    """It's easy - request.cls is the test class using the fixture, so request.cls.driver = ...
    is essentially the same as MyTestClass.driver = ... if MyTestClass uses the fixture.
    https://pytest.readthedocs.io/en/2.8.7/builtin.html"""
    before_failed = request.session.testsfailed
# te akcje zostaną wykonane  po wykonaniu akcji z plików z testami:
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()
