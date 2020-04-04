
from selenium.webdriver.common.by import By
from pages.base_actions import BaseActions

class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_actions = BaseActions(driver)
        self.welcome_message = (By.CSS_SELECTOR, "h3.RTL")

    def account_page_action(self):
        self.base_actions.assert_text_elements(self.welcome_message)
