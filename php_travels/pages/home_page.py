
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_menu = (By.CSS_SELECTOR, "ul .nav #li_myaccount")
        self.login_link = (By.CSS_SELECTOR, ".open >ul>:nth-child(1) > a")
        self.sign_up_link = (By.CSS_SELECTOR, ".open >ul>:nth-child(2) > a")

    def choose_home_page_action(self, driver, login="", sign_up=""):
        self.driver.find_element_by_css_selector(self.my_account_menu).click()
        driver.implicitly_wait(2)
        if login == True:
            self.driver.find_element_by_css_selector(self.login_link).click()
        elif sign_up == True:
            self.driver.find_element_by_css_selector(self.sign_up_link).click()


        # self.driver.find_element_by_css_selector(self.name_input).send_keys('Kazik')
        # self.driver.find_element_by_css_selector(self.lastname_input).send_keys('Ciacho')
        # self.driver.find_element_by_css_selector(self.phone_input).send_keys('123456789')
        # self.driver.find_element_by_css_selector(self.email_input).send_keys(email)
        # self.driver.find_element_by_css_selector(self.password_input).send_keys('Kazik9')
        # self.driver.find_element_by_css_selector(self.confirmpassword_input).send_keys('Kazik9')
        # time.sleep(2)
        # self.driver.find_element_by_css_selector(self.signup_button).click()
        # time.sleep(2)



