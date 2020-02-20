import time


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_button = "ul .nav #li_myaccount"
        self.login_button = ".open >ul>:nth-child(1) > a"
        self.email_input = "[name='username']"
        self.password_input = "[name='password']"
        self.checkbox_remember = "#remember-me"
        self.login_submit = ".loginbtn[type='submit']"
        self.reset_password = "div.col-md-12:nth-child(3)"
        self.reset_password_input = "[placeholder='your@email.com']"
        self.reset_password_button = "button.resetbtn"
        self.assert_login_submit_empty = ".resultlogin .alert-danger"
        self.assert_left_menu = ".nav.profile-tabs [data-toggle='tab']"
        self.assert_result_reset = ".alert-success"
        self.logout_button = ".open > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)"
        self.assert_logout = ".panel-heading"
        self.login_button_logout = "ul.navbar-side:nth-child(1) > li:nth-child(1) > a:nth-child(1)"


    def login_happy_path(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/')
        self.driver.find_element_by_css_selector(self.my_account_button).click()
        self.driver.find_element_by_css_selector(self.login_button).click()
        self.driver.find_element_by_css_selector(self.email_input).send_keys('sr@wp.pl')
        self.driver.find_element_by_css_selector(self.password_input).send_keys('123456789')
        self.driver.find_element_by_css_selector(self.checkbox_remember).click()
        self.driver.find_element_by_css_selector(self.login_submit).click()

    def login_forget_password(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/login')
        self.driver.find_element_by_css_selector(self.reset_password).click()
        self.driver.find_element_by_css_selector(self.reset_password_input).send_keys('s.r@wp.pl')
        self.driver.find_element_by_css_selector(self.reset_password_button).click()

    def login_empty_email(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/login')
        self.driver.find_element_by_css_selector(self.password_input).send_keys('123456789')
        self.driver.find_element_by_css_selector(self.login_submit).click()

    def login_empty_password(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/login')
        self.driver.find_element_by_css_selector(self.email_input).send_keys('sr@wp.pl')
        self.driver.find_element_by_css_selector(self.login_submit).click()

    def logout(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/login')
        self.driver.find_element_by_css_selector(self.email_input).send_keys('sr@wp.pl')
        self.driver.find_element_by_css_selector(self.password_input).send_keys('123456789')
        self.driver.find_element_by_css_selector(self.login_submit).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(self.login_button_logout).click()
        self.driver.find_element_by_css_selector(self.logout_button).click()
        time.sleep(1)

    def login_wrong_email(self):
        self.driver.get('http://www.kurs-selenium.pl/demo/login')
        self.driver.find_element_by_css_selector(self.email_input).send_keys('srwp.pl')
        self.driver.find_element_by_css_selector(self.password_input).send_keys('123456789')
        self.driver.find_element_by_css_selector(self.login_submit).click()

    def left_menu_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_left_menu)
        return [elements[x].text for x in range(len(elements))]

    def reset_password_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_result_reset)
        return [elements[x].text for x in range(len(elements))]

    def empty_email_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_login_submit_empty)
        return [elements[x].text for x in range(len(elements))]

    def empty_password_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_login_submit_empty)
        return [elements[x].text for x in range(len(elements))]

    def logout_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_logout)
        return [elements[x].text for x in range(len(elements))]

    def wrong_email_text(self):
        elements = self.driver.find_elements_by_css_selector(self.assert_login_submit_empty)
        return [elements[x].text for x in range(len(elements))]


