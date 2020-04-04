import time

from php_travels.pages.base_actions import BaseActions


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.base_actions = BaseActions(driver)

        self.checkbox_remember_me = "#remember-me"
        self.login_submit_button = ".loginbtn[type='submit']"
        self.email_input = "[name='username']"
        self.password_input = "[name='password']"
        self.forget_password_button = "div.col-md-12:nth-child(3)"
        self.reset_password_input = "[placeholder='your@email.com']"
        self.reset_password_button = "button.resetbtn"
        self.user_button_after_login = "ul.navbar-side:nth-child(1) > li:nth-child(1) > a:nth-child(1)"
        self.logout_button = ".open > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)"
        # Selectors for asserts:
        self.allert_messege_invalid_data = ".resultlogin .alert-danger"
        self.left_menu_tabs_names = ".nav.profile-tabs [data-toggle='tab']"
        self.allert_messege_success_sent = ".alert-success"
        self.allert_messege_invalid_email = ".alert"
        self.panel_heading_with_name_login = ".panel-heading"

    def login(self, email_data="", password_data=""):
        time.sleep(0.2)
        if email_data != "":
            self.base_actions.field_send_keys(self.email_input, email_data)
        if password_data != "":
            self.base_actions.field_send_keys(self.password_input, password_data)
        self.base_actions.click_on(self.checkbox_remember_me)
        self.base_actions.click_on(self.login_submit_button)

    def login_forget_password(self, email):
        time.sleep(0.5)
        self.base_actions.click_on(self.forget_password_button)
        self.base_actions.field_send_keys(self.reset_password_input, email)
        self.base_actions.click_on(self.reset_password_button)

    def logout(self, email_data, password_data):
        self.login(email_data, password_data)
        time.sleep(0.5)
        self.base_actions.click_on(self.user_button_after_login)
        self.base_actions.click_on(self.logout_button)

    def left_menu_text(self):
        return self.base_actions.assert_text_elements(self.left_menu_tabs_names)

    def reset_password_text(self):
        return self.base_actions.assert_text_elements(self.allert_messege_success_sent)

    def reset_password_wrong_mail_text(self):
        return self.base_actions.assert_text_elements(self.allert_messege_invalid_email)

    def empty_email_text(self):
        return self.base_actions.assert_text_elements(self.allert_messege_invalid_data)

    def empty_password_text(self):
        return self.base_actions.assert_text_elements(self.allert_messege_invalid_data)

    def wrong_email_text(self):
        return self.base_actions.assert_text_elements(self.allert_messege_invalid_data)

    def logout_text(self):
        return self.base_actions.assert_text_elements(self.panel_heading_with_name_login)
