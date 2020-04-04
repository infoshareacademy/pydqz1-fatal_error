import pytest
from assertpy import assert_that
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage
from helpers.generators import name_generator, surname_generator, phone_number_generator, email_generator, password_generator
import time
import allure

@allure.description('Testing My Account Menu')
@pytest.mark.usefixtures('setup')

class TestMyAccountMenu:
    @allure.step('Test if choosing Sign Up button in My Account Menu navigates to register page')
    def test_my_account_menu_flow(self):
        home_page = HomePage(self.driver)
        register_page = RegisterPage(self.driver)
        home_page.choose_home_page_action()
        header_text = register_page.register_page_header()

        assert_that(header_text).is_equal_to('Sign Up')


@allure.description('Testing register feature')
@pytest.mark.usefixtures('setup1')

class TestRegister:
# pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
    @allure.step('Test register with valid data')
    def test_register_valid_data(self):
        register_page = RegisterPage(self.driver)
        account_page = AccountPage(self.driver)
        name = name_generator()
        surname = surname_generator()
        number = phone_number_generator()
        email = email_generator()
        password = password_generator()
        password2 = password
        register_page.register_page_actions(self, name, surname, number, email, password, password2)

        account_welcome_message = account_page.account_page_action()
        account_welcome_message2= len("Hi, " + name + " " + surname)
        assert_that(account_welcome_message).is_equal_to(account_welcome_message2)

    # @allure.step('Test register with existing user email')
    # def test_same_email(self):
    #     register_page = RegisterPage(self.driver)
    #     name = name_generator()
    #     surname = surname_generator()
    #     number = phone_number_generator()
    #     email = email_generator()
    #     password = password_generator()
    #     password2 = password
    #     register_page.register_page_actions(name, surname, number, email, password, password2)
    #
