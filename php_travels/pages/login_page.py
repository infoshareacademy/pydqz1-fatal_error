import time
from selenium.webdriver.common.keys import Keys
from php_travels.pages.base_actions import BaseActions


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_button = "ul .nav #li_myaccount"
        self.login_button = ".open >ul>:nth-child(1) > a"
        self.checkbox_remember_me = "#remember-me"
        self.login_submit_button = ".loginbtn[type='submit']"
        self.email_input = "[name='username']"
        self.password_input = "[name='password']"
        self.forget_password_button = "div.col-md-12:nth-child(3)"
        self.reset_password_input = "[placeholder='your@email.com']"
        self.reset_password_button = "button.resetbtn"
        self.assert_after_bad_login = ".resultlogin .alert-danger"
        self.assert_after_sucess_login = ".nav.profile-tabs [data-toggle='tab']"
        self.assert_for_password_reset_result = ".alert-success"
        self.assert_for_password_reset_result_with_wrong_mail = ".alert"
        self.logout_button = ".open > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)"
        self.assert_for_logout_result = ".panel-heading"
        self.user_button_after_login = "ul.navbar-side:nth-child(1) > li:nth-child(1) > a:nth-child(1)"

    def login_happy_path(self, email_data, password_data):
        BaseActions.www_open(self)
        BaseActions.my_account_btn(self)
        BaseActions.login_btn(self)
        time.sleep(1)
        BaseActions.email_input(self, email_data)
        BaseActions.password_input(self, password_data)
        BaseActions.checkbox_remember_set(self)
        BaseActions.login_submit_btn(self)

    def login_forget_password(self, used_mail_data):
        BaseActions.www_open_login(self)
        time.sleep(1)
        BaseActions.forget_password_btn(self)
        BaseActions.reset_password_input(self, used_mail_data)
        BaseActions.reset_password_btn(self)

    def login_reset_password_wrong_mail(self, wrong_mail_data):
        BaseActions.www_open_login(self)
        time.sleep(1)
        BaseActions.forget_password_btn(self)
        BaseActions.reset_password_input_wrong(self, wrong_mail_data)
        BaseActions.reset_password_btn(self)

    def login_empty_email(self, password_data):
        BaseActions.www_open_login(self)
        time.sleep(1)
        BaseActions.password_input(self, password_data)
        BaseActions.login_submit_btn(self)

    def login_empty_password(self, email_data):
        BaseActions.www_open_login(self)
        time.sleep(1)
        BaseActions.email_input(self, email_data)
        BaseActions.login_submit_btn(self)

    def logout(self, email_data, password_data):
        BaseActions.www_open_login(self)
        time.sleep(1)
        BaseActions.email_input(self, email_data)
        BaseActions.password_input(self, password_data)
        BaseActions.login_submit_btn(self)
        time.sleep(1)
        BaseActions.user_btn(self)
        BaseActions.logout_btn(self)
        time.sleep(1)

    def login_wrong_email(self, wrong_mail_data, password_data):
        BaseActions.www_open_login(self)
        time.sleep(1)
        BaseActions.wrong_email_input(self, wrong_mail_data)
        BaseActions.password_input(self, password_data)
        BaseActions.login_submit_btn(self)

    def left_menu_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_after_sucess_login)
        return [elements[x].text for x in range(len(elements))]

    def reset_password_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_for_password_reset_result)
        return [elements[x].text for x in range(len(elements))]

    def reset_password_wrong_mail_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_for_password_reset_result_with_wrong_mail)
        return [elements[x].text for x in range(len(elements))]

    def empty_email_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_after_bad_login)
        return [elements[x].text for x in range(len(elements))]

    def empty_password_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_after_bad_login)
        return [elements[x].text for x in range(len(elements))]

    def logout_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_for_logout_result)
        return [elements[x].text for x in range(len(elements))]

    def wrong_email_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_after_bad_login)
        return [elements[x].text for x in range(len(elements))]
