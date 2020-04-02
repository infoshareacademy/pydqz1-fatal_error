import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ..pages.locators import CommonSignInLocators as Locators
class HomePage:

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)       #wywołanie konstruktora klasy bazowej
        # self.my_account_menu_css = "ul .nav #li_myaccount"
        # self.sign_up_link_css = ".open >ul>:nth-child(2) > a"
        # self.name_input = "[name='firstname']"
        # self.lastname_input = "[name='lastname']"
        # self.phone_input = "[name='phone']"
        # self.email_input = "[name='email']"
        # self.password_input = "[name='password']"
        # self.confirmpassword_input = "[name='confirmpassword']"
        # self.signup_button = "button.signupbtn.btn_full.btn.btn-action.btn-block.btn-lg"
        # self.my_profile_text = "div#body-section li:nth-child(2) > a"
        # #następne css selektory

    def unfold_my_account_menu(self):
        return self.driver.find_element(*Locators.MY_ACCOUNT_MENU)

    def choose__to_sign_in(self):
        return self.driver.find_element(*Locators.SIGN_UP_LINK)

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


    # nastepne metody dostepne na tej stronie

    # metody mogą także obejmować pobranie i zapisanie w liście danych dostepnych na stronie:

    def text_left_menu(self):
        elements = self.driver.find_elements_by_css_selector(self.my_profile_text)
        return [elements[x].text for x in range(len(elements))]
