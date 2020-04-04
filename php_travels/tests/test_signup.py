import pytest
from selenium.webdriver.support.ui import Select
from assertpy import assert_that
from pages.home_page import HomePage
from pages.register_page import SignUpPage
from pages.account_page import AccountPage
import time
import allure

@allure.description('Testing Sign up feature')
# klasa z testami dotyczącymi jednej funkcjonalności:
@pytest.mark.usefixtures('setup')
class TestSignUpPage:

# pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
    def sign_up_setup(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/')
        home_page = HomePage(self.driver)                  # -> stworzenie page objectu z przypisaniem mu webdrivera
        home_page.home_page_actions()                      # -> wywołanie zamierzonej akcji na stronie
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.sign_up_page_actions()
        account_page = AccountPage(self.driver)
        account_page.account_page_actions()




        time.sleep(2)
        list_of_assert_elements = home_page.text_left_menu()
        assert list_of_assert_elements == ["My Profile"]   # assercja na metodzie zwracająco liste elementów
        # np. listę samochodów ze strony z moją oczekiwaną listą samochodów


    def test_same_email(self):
        home_page = HomePage(self.driver)
        home_page.home_page_actions(firstname='name', lastname='surname', phone='phone',  )

