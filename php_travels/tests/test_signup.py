import pytest
from selenium.webdriver.support.ui import Select
from assertpy import assert_that
from pages.home_page import HomePage
import time
import allure

@allure.description('Testing Sign up feature')
# klasa z testami dotyczącymi jednej funkcjonalności:
@pytest.mark.usefixtures('setup')
class TestSignUpPage:

# pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
    def test_numerouno(self):
        home_page = HomePage(self.driver)  # -> stworzenie page objectu z przypisaniem mu webdrivera
        home_page.action_on_page()  # -> wywołanie zamierzonej akcji na stronie

        time.sleep(2)
        list_of_assert_elements = home_page.text_left_menu()
        assert list_of_assert_elements == ["My Profile"]   # assercja na metodzie zwracająco liste elementów
        # np. listę samochodów ze strony z moją oczekiwaną listą samochodów


    def test_same_email(self):
        home_page = HomePage(self.driver)
        home_page.action_on_page(firstname='Kazik', lastname='Ciacho', phone='phone',  )

