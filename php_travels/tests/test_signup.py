import pytest
from assertpy import assert_that
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage
from helpers import generators
import time
import allure



@allure.description('Testing Register feature')
@pytest.mark.usefixtures('setup')
# klasa z testami dotyczącymi jednej funkcjonalności
class TestRegister:

# pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
    @allure.step('Test register with valid data')
    def test_register_valid_data(self, name=name_generator(), surname="", number, email, password):
        self.home_page.




        time.sleep(2)
        list_of_assert_elements = home_page.text_left_menu()
        assert list_of_assert_elements == ["My Profile"]   # assercja na metodzie zwracająco liste elementów
        # np. listę samochodów ze strony z moją oczekiwaną listą samochodów


    def test_same_email(self):
        home_page = HomePage(self.driver)
        home_page.home_page_actions(firstname='name', lastname='surname', phone='phone',  )

