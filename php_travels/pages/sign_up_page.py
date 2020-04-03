from pages.sign_up_data import SignUpData
from pages.locators import CommonSignInLocators as Locators
from tests.test_signup import TestSignUpPage

class SignUpPage(TestSignUpPage):


    def __init__(self,driver):
        super(SignUpPage, self).__init__(driver)

    def find_name_input(self):
            return self.driver.find_element(*Locators.NAME_INPUT)

    def find_last_name_input(self):
        return self.driver.find_element(*Locators.LAST_NAME_INPUT)

    def find_mobile_number_input(self):
        return self.driver.find_element(*Locators.PHONE_INPUT)

    def find_email_input(self):
        return self.driver.find_element(*Locators.EMAIL_INPUT)

    def find_password_input(self):
        return self.driver.find_element(*Locators.PASSWORD_INPUT)

    def find_confirm_password_input(self):
        return self.driver.find_element(*Locators.CONFIRM_PASSWORD_INPUT)

    def find_sign_up_button(self):
        return self.driver.find_element(*Locators.SIGN_UP_BUTTON)\

    def sign_up_page_actions(self, driver):
        sign_up = SignUpData()
        self.find_name_input().send_keys(sign_up.first_name_input)
        self.find_last_name_input().send_keys(sign_up.last_name_input)
        self.find_mobile_number_input().send_keys(sign_up.mobile_number_input)
        self.find_email_input().send_keys(sign_up.email_input)
        self.find_password_input().send_keys(sign_up.password_input)
        self.find_confirm_password_input().send_keys(sign_up.confirm_password_input)
        driver.implicitly_wait(3)
        self.find_sign_up_button().click()
