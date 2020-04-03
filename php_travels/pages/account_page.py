from tests.test_signup import TestSignUpPage
from pages.locators import CommonSignInLocators as Locators
class AccountPage(TestSignUpPage):

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver)       #wywołanie konstruktora klasy bazowej

    def find_my_profile_text(self):
        return self.driver.find_elements(*Locators.MY_PROFILE_TEXT)

    def account_page_actions(self):
        elements = self.find_my_profile_text()
        return [elements[x].text for x in range(len(elements))]
