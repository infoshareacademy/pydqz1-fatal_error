
from selenium.webdriver.common.by import By
from pages.base_actions import BaseActions

class RegisterPage:


    def __init__(self, driver):
        self.driver = driver
        self.base_actions = BaseActions(driver)
        self.name_input = (By.CSS_SELECTOR, "[name='firstname']")
        self.last_name_input = (By.CSS_SELECTOR, "[name='lastname']")
        self.phone_input = (By.CSS_SELECTOR, "[name='phone']")
        self.email_input = (By.CSS_SELECTOR, "[name='email']")
        self.password_input = (By.CSS_SELECTOR, "[name='password']")
        self.confirm_password_input = (By.CSS_SELECTOR, "[name='confirmpassword']")
        self.sign_up_button = (By.CSS_SELECTOR, "button.signupbtn.btn_full.btn.btn-action.btn-block.btn-lg")

    def sign_up_page_actions(self, driver, name, surname, number, email, password, password2):
        if name != "":
            self.base_actions.field_send_keys(self.name_input, name)                     #self.driver.find_element_by_css_selector(self.name_input).send_keys(name)
        if surname != "":
            self.base_actions.field_send_keys(self.last_name_input, surname)             #self.driver.find_element_by_css_selector(self.last_name_input).send_keys(surname)
        if number != "":
            self.base_actions.field_send_keys(self.phone_input, number)                  #self.driver.find_element_by_css_selector(self.phone_input).send_keys(number)
        if email != "":
            self.base_actions.field_send_keys(self.email_input, email)                   #self.driver.find_element_by_css_selector(self.email_input).send_keys(email)
        if password != "":
            self.base_actions.field_send_keys(self.password_input, password)             #self.driver.find_element_by_css_selector(self.password_input).send_keys(password)
        if password2 != "":
            self.base_actions.field_send_keys(self.confirm_password_input, password2)    #self.driver.find_element_by_css_selector(self.confirm_password_input).send_keys(password2)
        driver.implicitly_wait(3)
        self.base_actions.click_on(self.sign_up_button)                                  #self.driver.find_element_by_css_selector(self.sign_up_button).click()
