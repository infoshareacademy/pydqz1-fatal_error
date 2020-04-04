import time
from selenium.webdriver.common.by import By
from pages.base_actions import BaseActions

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_actions = BaseActions(driver)
        self.my_account_menu = (By.CSS_SELECTOR, "ul .nav #li_myaccount")
        self.login_link = (By.CSS_SELECTOR, ".open >ul>:nth-child(1) > a")
        self.sign_up_link = (By.CSS_SELECTOR, ".open >ul>:nth-child(2) > a")

    def choose_home_page_action(self, button_name="login"):
        self.base_actions.click_on(self.my_account_menu)               # self.driver.find_element_by_css_selector(self.my_account_menu).click()
        time.sleep(2)
        if button_name == "login":
            self.base_actions.click_on(self.login_link)                #self.driver.find_element_by_css_selector(self.login_link).click()
        else:
            self.base_actions.click_on(self.sign_up_link)              #self.driver.find_element_by_css_selector(self.sign_up_link).click()
