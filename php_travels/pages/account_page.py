import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pages.locators import CommonSignInLocators as Locators
class AccountPage():

    def __init__(self, driver):
        super(AccountPage, self).__init__(driver)       #wywołanie konstruktora klasy bazowej

    def find_my_profile_text(self):
        elements = self.driver.find_elements(*Locators.MY_PROFILE_TEXT)
        return [elements[x].text for x in range(len(elements))]
