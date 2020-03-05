class BaseActions:

    def www_open(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/')

    def www_open_login(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/login')

    def my_account_btn(self):
        self.driver.find_element_by_css_selector(self.my_account_button).click()

    def login_btn(self):
        self.driver.find_element_by_css_selector(self.login_button).click()

    def checkbox_remember_set(self):
        self.driver.find_element_by_css_selector(self.checkbox_remember_me).click()

    def login_submit_btn(self):
        self.driver.find_element_by_css_selector(self.login_submit_button).click()

    def email_input(self, email_data):
        self.driver.find_element_by_css_selector(self.email_input).send_keys(email_data)

    def wrong_email_input(self, wrong_mail_data):
        self.driver.find_element_by_css_selector(self.email_input).send_keys(wrong_mail_data)

    def password_input(self, password_data):
        self.driver.find_element_by_css_selector(self.password_input).send_keys(password_data)

    def forget_password_btn(self):
        self.driver.find_element_by_css_selector(self.forget_password_button).click()

    def reset_password_input(self, used_mail_data):
        self.driver.find_element_by_css_selector(self.reset_password_input).send_keys(used_mail_data)

    def reset_password_input_wrong(self, wrong_mail_data):
        self.driver.find_element_by_css_selector(self.reset_password_input).send_keys(wrong_mail_data)

    def reset_password_btn(self):
        self.driver.find_element_by_css_selector(self.reset_password_button).click()

    def user_btn(self):
        self.driver.find_element_by_css_selector(self.user_button_after_login).click()

    def logout_btn(self):
        self.driver.find_element_by_css_selector(self.logout_button).click()
