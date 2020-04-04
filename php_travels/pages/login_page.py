import time

from php_travels.pages.base_actions import BaseActions


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.base_actions = BaseActions(driver)
        self.my_account_button = "ul .nav #li_myaccount"
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
        self.base_actions.click_on(self.my_account_button)
        time.sleep(0.2)
        self.base_actions.field_send_keys(self.email_input, email_data)
        self.base_actions.field_send_keys(self.password_input, password_data)
        self.base_actions.click_on(self.checkbox_remember_me)
        self.base_actions.click_on(self.login_submit_button)

    def login_forget_password(self, used_email_data):
        time.sleep(0.2)
        self.base_actions.click_on(self.forget_password_button)
        self.base_actions.field_send_keys(self.reset_password_input, used_email_data)
        self.base_actions.click_on(self.reset_password_button)

    def login_reset_password_wrong_mail(self, wrong_mail_data):
        time.sleep(0.2)
        self.base_actions.click_on(self.forget_password_button)
        self.base_actions.field_send_keys(self.reset_password_input, wrong_mail_data)
        self.base_actions.click_on(self.reset_password_button)

    def login_empty_email(self, password_data):
        self.base_actions.field_send_keys(self.password_input, password_data)
        self.base_actions.click_on(self.login_submit_button)

    def login_empty_password(self, email_data):
        self.base_actions.field_send_keys(self.email_input, email_data)
        self.base_actions.click_on(self.login_submit_button)

    def logout(self, email_data, password_data):
        self.base_actions.field_send_keys(self.email_input, email_data)
        self.base_actions.field_send_keys(self.password_input, password_data)
        self.base_actions.click_on(self.login_submit_button)
        time.sleep(0.2)
        self.base_actions.click_on(self.user_button_after_login)
        self.base_actions.click_on(self.logout_button)

    def login_wrong_email(self, wrong_mail_data, password_data):
        self.base_actions.field_send_keys(self.email_input, wrong_mail_data)
        self.base_actions.field_send_keys(self.password_input, password_data)
        self.base_actions.click_on(self.login_submit_button)

    def left_menu_text(self):
        return self.base_actions.assert_text_elements(self.assert_after_sucess_login)

    def reset_password_text(self):
        return self.base_actions.assert_text_elements(self.assert_for_password_reset_result)

    def reset_password_wrong_mail_text(self):
        return self.base_actions.assert_text_elements(self.assert_for_password_reset_result_with_wrong_mail)

    def empty_email_text(self):
        return self.base_actions.assert_text_elements(self.assert_after_bad_login)

    def empty_password_text(self):
        return self.base_actions.assert_text_elements(self.assert_after_bad_login)

    def logout_text(self):
        return self.base_actions.assert_text_elements(self.assert_for_logout_result)

    def wrong_email_text(self):
        return self.base_actions.assert_text_elements(self.assert_after_bad_login)
