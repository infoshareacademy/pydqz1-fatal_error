import time


class PageOne:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_menu_css = "ul .nav #li_myaccount"
        self.sign_up_link_css = ".open >ul>:nth-child(2) > a"
        self.sign_up_text = "Sign Up"
        self.name_input = "[name='firstname']"
        self.lastname_input = "[name='lastname']"
        self.phone_input = "[name='phone']"
        self.email_input = "[name='email']"
        self.password_input = "[name='password']"
        self.confirmpassword_input = "[name='confirmpassword']"
        self.signup_button = "button.signupbtn.btn_full.btn.btn-action.btn-block.btn-lg"
        #następne css selektory

    def action_on_page(self):
        self.driver.find_element_by_css_selector(self.my_account_menu_css).click()
        self.driver.find_element_by_css_selector(self.sign_up_link_css).click()
        self.driver.find_element_by_css_selector(self.name_input).send_keys('Kazik')
        self.driver.find_element_by_css_selector(self.lastname_input).send_keys('Ciacho')
        self.driver.find_element_by_css_selector(self.phone_input).send_keys('123456789')
        self.driver.find_element_by_css_selector(self.email_input).send_keys('ciacho@wp.pl')
        self.driver.find_element_by_css_selector(self.password_input).keus_input('Kazik1')
        self.driver.find_element_by_css_selector(self.confirmpassword_input).send_keys('Kazik1')
        time.sleep(5)
        self.driver.find_element_by_css_selector(self.signup_button).click()
        time.sleep(2)


    # nastepne metody dostepne na tej stronie

    # metody mogą także obejmować pobranie i zapisanie w liście danych dostepnych na stronie:

    def text_on_page(self):
        elements = self.driver.find_elements_by_css_selector(self.sign_up_text)

        return [elements[x].text for x in range(len(elements))]  # czy ktoś jeszcze pamięta list comprehension? ;)
