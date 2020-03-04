import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.page_one import SearchFeature


@pytest.fixture()
def setup(request):
    # te akcje zostsaną wykonane przed testem:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.kurs-selenium.pl/demo/')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.search_feature = SearchFeature(driver)
    # te akcje zostaną po wykonaniu akcji z plików z testami:
    yield
    driver.quit()


#
# @pytest.fixture()
# def setup(request):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get('http://localhost:8080')
#     driver.implicitly_wait(10)
#     request.cls.driver = driver
#     request.cls.login_page = LoginPage(driver)
#     request.cls.nav = Navbar(driver)
#     before_failed = request.session.testsfailed
#     yield
#     if request.session.testsfailed != before_failed:
#         allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
#     driver.quit()
