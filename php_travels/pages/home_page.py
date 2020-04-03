import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.locators import CommonSignInLocators as Locators
class HomePage:

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)       #wywołanie konstruktora klasy bazowej

    def find_my_account_menu(self):
        return self.driver.find_element(*Locators.MY_ACCOUNT_MENU)

    def find_sign_up_link(self):
        return self.driver.find_element(*Locators.SIGN_UP_LINK)

    def home_page_actions(self,driver):
        self.find_my_account_menu().click()
        driver.implicitly_wait(2)
        self.find_sign_up_link().click()

        # self.driver.find_element_by_css_selector(self.my_account_menu_css).click()
        # self.driver.find_element_by_css_selector(self.sign_up_link_css).click()
        # self.driver.find_element_by_css_selector(self.name_input).send_keys('Kazik')
        # self.driver.find_element_by_css_selector(self.lastname_input).send_keys('Ciacho')
        # self.driver.find_element_by_css_selector(self.phone_input).send_keys('123456789')
        # self.driver.find_element_by_css_selector(self.email_input).send_keys(email)
        # self.driver.find_element_by_css_selector(self.password_input).send_keys('Kazik9')
        # self.driver.find_element_by_css_selector(self.confirmpassword_input).send_keys('Kazik9')
        # time.sleep(2)
        # self.driver.find_element_by_css_selector(self.signup_button).click()
        # time.sleep(2)



